'use client';

import { Button } from '../../components/ui/button';
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
    DialogTrigger
} from '../../components/ui/dialog';
import { useTheme } from 'next-themes';
import React, { useState } from 'react';
import SyntaxHighlighter from 'react-syntax-highlighter';
import {
    gruvboxDark,
    gruvboxLight
} from 'react-syntax-highlighter/dist/esm/styles/hljs';
import LoadingSpinner from '../loadingspinners/loadingspinner';

const CodeSolution = ({
    solution_link,
    problem_name
}: {
    solution_link: string;
    problem_name: string;
}) => {
    const [content, setContent] = useState('');
    const { theme } = useTheme();
    const [isloading, setIsloading] = useState(false);

    return (
        <Dialog>
            <DialogTrigger asChild>
                <Button
                    variant="default"
                    onClick={async () => {
                        setIsloading(true);
                        try {
                            const text = await fetch(solution_link);
                            const data = await text.text();
                            setContent(() => data);
                            setIsloading(false);
                        } catch (err) {
                            setIsloading(false);
                        }
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
                {isloading ? (
                    <LoadingSpinner name="solution" />
                ) : (
                    <SyntaxHighlighter
                        language="python"
                        style={theme === 'light' ? gruvboxLight : gruvboxDark}
                    >
                        {content}
                    </SyntaxHighlighter>
                )}
            </DialogContent>
        </Dialog>
    );
};

export default React.memo(CodeSolution);
// export default CodeSolution;
