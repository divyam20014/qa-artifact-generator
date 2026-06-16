import * as XLSX from 'xlsx';
import { TestCase, ProjectState } from '@/context/ProjectContext';

export const exportToExcel = (testCases: TestCase[]) => {
  const worksheet = XLSX.utils.json_to_sheet(
    testCases.map((tc) => ({
      'Test Case ID': tc.testCaseId,
      Title: tc.title,
      Type: tc.type,
      'Pre Conditions': tc.preConditions,
      Steps: tc.steps.join('\n'),
      'Expected Result': tc.expectedResult,
    }))
  );

  const columnWidths = [{ wch: 15 }, { wch: 30 }, { wch: 12 }, { wch: 40 }, { wch: 50 }, { wch: 40 }];
  worksheet['!cols'] = columnWidths;

  const workbook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workbook, worksheet, 'Test Cases');
  XLSX.writeFile(workbook, 'qa-test-cases.xlsx');
};

export const exportToMarkdown = (testCases: TestCase[]) => {
  const markdown = `# QA Test Cases\n\n${testCases.map((tc) => `## ${tc.testCaseId}: ${tc.title}\n\n**Type:** ${tc.type}\n\n**Pre Conditions:** ${tc.preConditions}\n\n**Steps:**\n${tc.steps.map((step) => `- ${step}`).join('\n')}\n\n**Expected Result:** ${tc.expectedResult}\n\n---`).join('\n\n')}`;

  const blob = new Blob([markdown], { type: 'text/markdown' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'qa-test-cases.md';
  a.click();
  URL.revokeObjectURL(url);
};

export const exportProjectState = (state: ProjectState) => {
  const blob = new Blob([JSON.stringify(state, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `qa-project-export-${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
  URL.revokeObjectURL(url);
};

export const importProjectState = (file: File): Promise<ProjectState> => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      try {
        const state = JSON.parse(e.target?.result as string) as ProjectState;
        resolve(state);
      } catch (error) {
        reject(new Error('Invalid project file format'));
      }
    };
    reader.onerror = () => reject(new Error('Failed to read file'));
    reader.readAsText(file);
  });
};
