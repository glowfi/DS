import { createContext, useContext } from 'react';
import { Itheme } from './topic-table';

const ThemeCtx = createContext<Itheme | undefined>(undefined);

export function useThemeCtx() {
    const theme = useContext(ThemeCtx);
    if (theme === undefined) {
        throw new Error('Some Error occured!');
    }
    return theme;
}

export default ThemeCtx;
