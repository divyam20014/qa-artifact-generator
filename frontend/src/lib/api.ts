const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface UploadResponse {
  status: string;
  filename: string;
  rawText: string;
}

export const uploadFile = async (file: File): Promise<UploadResponse> => {
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch(`${API_URL}/api/upload`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || 'Failed to upload file');
  }

  return response.json();
};

export const analyzeGaps = async (rawText: string) => {
  const response = await fetch(`${API_URL}/api/analyze-gaps`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ rawText }),
  });

  if (!response.ok) throw new Error('Failed to analyze gaps');
  return response.json();
};

export const generateCriteria = async (modules: any[]) => {
  const response = await fetch(`${API_URL}/api/generate-criteria`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ modules }),
  });

  if (!response.ok) throw new Error('Failed to generate criteria');
  return response.json();
};

export const generateScenarios = async (criteria: any[]) => {
  const response = await fetch(`${API_URL}/api/generate-scenarios`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ criteria }),
  });

  if (!response.ok) throw new Error('Failed to generate scenarios');
  return response.json();
};

export const generateTestCases = async (scenarios: any[]) => {
  const response = await fetch(`${API_URL}/api/generate-testcases`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ scenarios }),
  });

  if (!response.ok) throw new Error('Failed to generate test cases');
  return response.json();
};
