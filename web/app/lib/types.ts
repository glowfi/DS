enum ApproachType {
    BRUTE = 'Brute',
    BETTER = 'Better',
    OPTIMAL = 'Optimal',
    RECURSION = 'Recursion',
    MEMOIZATION = 'Memoization',
    TABULATION = 'Tabulation',
    SPACEOPTIMIZED = 'Space Optimized'
}

export enum Difficulty {
    Easy = 'Easy',
    Medium = 'Medium',
    Hard = 'Hard'
}

export interface Approach {
    type: ApproachType;
    tc: string;
    sc: string;
    intuition: string;
    code: string;
}

export interface Question {
    id: number;
    topic: string;
    pattern: string;
    question: string;
    problem_name: string;
    problem_link: string;
    difficulty: Difficulty;
    difficulty_num: number;
    solution_link: string;
    language: string;
    approaches: Approach[];
}
