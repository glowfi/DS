import { Question } from './types';

export const getDifficultyColor = (difficulty: string) => {
    if (difficulty === 'Easy') {
        return 'green';
    } else if (difficulty === 'Medium') {
        return '#999900';
    } else {
        return 'red';
    }
};

export function getRandomHexColor(): string {
    const hex: string = '0123456789ABCDEF';
    let color: string = '#';
    for (let i = 0; i < 6; i++) {
        color += hex[Math.floor(Math.random() * 16)];
    }
    return color;
}

export function getPatternWiseRandomHexColor(questions: Question[]): {
    [pattern: string]: string;
} {
    const patternColors: { [pattern: string]: string } = {};

    questions.forEach((question: Question) => {
        const patterns = question.pattern.trim().split('/');
        patterns.forEach((pattern) => {
            if (!patternColors[pattern.trim()]) {
                // Trim each pattern
                patternColors[pattern.trim()] = getRandomHexColor();
            }
        });
    });

    return patternColors;
}

export function getRelativeLuminance(color: string): number {
    const hex = color.startsWith('#') ? color : `#${color}`;
    const r = parseInt(hex.slice(1, 3), 16) / 255;
    const g = parseInt(hex.slice(3, 5), 16) / 255;
    const b = parseInt(hex.slice(5, 7), 16) / 255;

    const rLinear =
        r <= 0.03928 ? r / 12.92 : Math.pow((r + 0.055) / 1.055, 2.4);
    const gLinear =
        g <= 0.03928 ? g / 12.92 : Math.pow((g + 0.055) / 1.055, 2.4);
    const bLinear =
        b <= 0.03928 ? b / 12.92 : Math.pow((b + 0.055) / 1.055, 2.4);

    return 0.2126 * rLinear + 0.7152 * gLinear + 0.0722 * bLinear;
}

export function getReadableTextColor(
    bgColor: string,
    isDarkMode: boolean
): string {
    const luminance = getRelativeLuminance(bgColor);
    const contrastRatio = isDarkMode ? 4.5 : 4.5; // Maintain a minimum contrast ratio for both modes

    let textColor: string;

    // Determine text color based on luminance
    if (luminance < 0.5) {
        textColor = '#fff'; // White text for dark backgrounds
    } else {
        textColor = '#000'; // Black text for light backgrounds
    }

    // Check if the selected text color meets the contrast ratio requirement
    const contrastWithWhite = getContrastRatio(
        luminance,
        getRelativeLuminance('#fff')
    );
    const contrastWithBlack = getContrastRatio(
        luminance,
        getRelativeLuminance('#000')
    );

    if (contrastWithWhite >= contrastRatio) {
        return '#fff'; // Use white if it meets the contrast requirement
    } else if (contrastWithBlack >= contrastRatio) {
        return '#000'; // Use black if it meets the contrast requirement
    }

    // Fallback to a default color if neither meets the requirement
    return textColor;
}

function getContrastRatio(luminance1: number, luminance2: number): number {
    const lighter = Math.max(luminance1, luminance2);
    const darker = Math.min(luminance1, luminance2);
    return (lighter + 0.05) / (darker + 0.05);
}
