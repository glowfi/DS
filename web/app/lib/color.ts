export const getDifficultyColor = (difficulty: string) => {
    if (difficulty === 'Easy') {
        return 'green';
    } else if (difficulty === 'Medium') {
        return '#999900';
    } else {
        return 'red';
    }
};
