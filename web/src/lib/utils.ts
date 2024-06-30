import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';
import { _THEME, THEME } from '../components/topics/code-themes';

export function cn(...inputs: ClassValue[]) {
    return twMerge(clsx(inputs));
}

export function searchInListOfLists(listOfLists: any, searchTerm: any) {
    const results: any = [];

    listOfLists.forEach((item: any) => {
        const score = calculateMatchingScore(JSON.stringify(item), searchTerm);
        if (score > 0) {
            results.push({ item, score });
        }
    });

    results.sort((a: any, b: any) => b.score - a.score);

    return results
        .slice(0, 6)
        .map((result: any) => JSON.parse(JSON.stringify(result.item)));
}

export function calculateMatchingScore(str: any, searchTerm: string) {
    if (typeof str !== 'string') {
        return 0;
    }
    const searchTermLower = searchTerm.toLowerCase();
    const strLower = str.toLowerCase();
    let score = 0;

    if (strLower.includes(searchTermLower)) {
        score += 1;
    }

    if (strLower.startsWith(searchTermLower)) {
        score += 2;
    }

    if (strLower === searchTermLower) {
        score += 3;
    }

    return score;
}

export const getColor = (difficulty: string) => {
    if (difficulty === 'Easy') {
        return 'green';
    } else if (difficulty === 'Medium') {
        return '#999900';
    } else {
        return 'red';
    }
};

export const getThemeIndex = (theme: string) => {
    for (let index = 0; index < THEME.length; index++) {
        if (theme === THEME[index]) {
            console.log('YEs');
            return _THEME[index];
        }
    }
    return -1;
};
