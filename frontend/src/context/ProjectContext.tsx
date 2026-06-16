'use client';

import { createContext, useContext, useState, ReactNode, useEffect } from 'react';

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

export interface ProjectState {
  rawText: string;
  modules: Module[];
  criteria: TestCriteria[];
  scenarios: TestScenario[];
  testCases: TestCase[];
  currentStep: number;
}

interface ProjectContextType {
  state: ProjectState;
  setState: (newState: Partial<ProjectState>) => void;
  resetState: () => void;
  loadState: (savedState: ProjectState) => void;
}

const ProjectContext = createContext<ProjectContextType | undefined>(undefined);
const STORAGE_KEY = 'qa-project-state';
const INITIAL_STATE: ProjectState = {
  rawText: '',
  modules: [],
  criteria: [],
  scenarios: [],
  testCases: [],
  currentStep: 1,
};

export const ProjectProvider = ({ children }: { children: ReactNode }) => {
  const [state, setState_internal] = useState<ProjectState>(INITIAL_STATE);
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    if (typeof window !== 'undefined') {
      try {
        const saved = sessionStorage.getItem(STORAGE_KEY);
        if (saved) {
          setState_internal(JSON.parse(saved));
        }
      } catch (error) {
        console.error('Failed to load state from sessionStorage:', error);
      }
    }
    setIsLoaded(true);
  }, []);

  useEffect(() => {
    if (isLoaded && typeof window !== 'undefined') {
      try {
        sessionStorage.setItem(STORAGE_KEY, JSON.stringify(state));
      } catch (error) {
        console.error('Failed to save state to sessionStorage:', error);
      }
    }
  }, [state, isLoaded]);

  const updateState = (newState: Partial<ProjectState>) => {
    setState_internal((prev) => ({ ...prev, ...newState }));
  };

  const resetState = () => {
    setState_internal(INITIAL_STATE);
    if (typeof window !== 'undefined') {
      sessionStorage.removeItem(STORAGE_KEY);
    }
  };

  const loadState = (savedState: ProjectState) => {
    setState_internal(savedState);
  };

  useEffect(() => {
    const handleBeforeUnload = () => {
      if (typeof window !== 'undefined') {
        sessionStorage.removeItem(STORAGE_KEY);
      }
    };

    window.addEventListener('beforeunload', handleBeforeUnload);
    return () => window.removeEventListener('beforeunload', handleBeforeUnload);
  }, []);

  return (
    <ProjectContext.Provider
      value={{ state, setState: updateState, resetState, loadState }}
    >
      {children}
    </ProjectContext.Provider>
  );
};

export const useProject = () => {
  const context = useContext(ProjectContext);
  if (!context) {
    throw new Error('useProject must be used within a ProjectProvider');
  }
  return context;
};
