export type Severity = 'High' | 'Medium' | 'Low';
export type ScenarioType = 'Positive' | 'Negative' | 'Edge Case';
export type TestCaseType = 'Positive' | 'Negative' | 'Edge Case';

export interface Gap {
  gapId: string;
  description: string;
  severity: Severity;
  impact: string;
  suggestedFix?: string;
}

export interface Module {
  moduleId: string;
  moduleName: string;
  summary: string;
  gaps: Gap[];
}

export interface TestCriteria {
  criteriaId: string;
  moduleId: string;
  description: string;
}

export interface TestScenario {
  scenarioId: string;
  criteriaId: string;
  scenarioType: ScenarioType;
  title: string;
}

export interface TestCase {
  testCaseId: string;
  scenarioId: string;
  title: string;
  type: TestCaseType;
  preConditions: string;
  steps: string[];
  expectedResult: string;
}
