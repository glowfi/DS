'use client';

import React from 'react';
import { Button } from '@/components/ui/button';
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
    DialogTrigger
} from '@/components/ui/dialog';
import { useTheme } from 'next-themes';
import { useState } from 'react';
import SyntaxHighlighter from 'react-syntax-highlighter';
import {
    gruvboxDark,
    gruvboxLight
} from 'react-syntax-highlighter/dist/esm/styles/hljs';

const CodeSolution = ({
    solution_link,
    problem_name
}: {
    solution_link: string;
    problem_name: string;
}) => {
    const [content, setContent] = useState('');
    const { theme } = useTheme();

    return (
        <Dialog>
            <DialogTrigger asChild>
                <Button
                    variant="default"
                    onClick={async () => {
                        try {
                            const text = await fetch(solution_link);
                            const data = await text.text();
                            setContent(() => data);
                        } catch (err) {}
                    }}
                >
                    See code
                </Button>
            </DialogTrigger>
            <DialogContent className="sm:max-w-full overflow-y-auto">
                <DialogHeader>
                    <DialogTitle>{problem_name}</DialogTitle>
                    <DialogDescription>Code Solution</DialogDescription>
                </DialogHeader>
                <SyntaxHighlighter
                    language="python"
                    style={theme === 'light' ? gruvboxLight : gruvboxDark}
                >
                    {content}
                </SyntaxHighlighter>
            </DialogContent>
        </Dialog>
    );
};

export default React.memo(CodeSolution);
