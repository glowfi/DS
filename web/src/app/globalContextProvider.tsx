'use client';
import React, { useState } from 'react';
import { gruvboxDark } from 'react-syntax-highlighter/dist/esm/styles/hljs';
import ThemeCtx from '../components/topics/code-theme-context';

const GlobalContextProvider = ({ children }: any) => {
    const [codetheme, setCodetheme] = useState(gruvboxDark);

    return (
        <ThemeCtx.Provider value={{ codetheme, setCodetheme }}>
            {children}
        </ThemeCtx.Provider>
    );
};

export default GlobalContextProvider;
