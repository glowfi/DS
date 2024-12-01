'use client';
import React, { useCallback, useState } from 'react';
import SyntaxHighlighter from 'react-syntax-highlighter';
import { Button } from '../../components/ui/button';
import {
    Dialog,
    DialogContent,
    DialogHeader,
    DialogTrigger
} from '../../components/ui/dialog';
import { getThemeIndex } from '../../lib/utils';
import LoadingSpinner from '../loadingspinners/loadingspinner';
import { useThemeCtx } from './code-theme-context';
import { ThemeDropdown } from './theme-dropdown';
import { CodeDropDown } from './code-dropdown';

interface CodeSolutionProps {
    solution_link: string;
    problem_name: string;
    changeLangauge: (language: string) => void;
}

const CodeSolution: React.FunctionComponent<CodeSolutionProps> = ({
    solution_link,
    changeLangauge
}) => {
    const [content, setContent] = useState<{ codeTxt: string }>({
        codeTxt: ''
    });
    const [isloading, setIsloading] = useState(false);
    const { codetheme, setCodetheme } = useThemeCtx();

    const fetchCode = useCallback(async () => {
        setIsloading(true);
        try {
            const text = await fetch(solution_link);
            const data = await text.text();
            setContent({ ...content, codeTxt: data });
            if (localStorage.getItem('code-theme')) {
                setCodetheme(
                    //@ts-ignore
                    getThemeIndex(
                        //@ts-ignore
                        localStorage.getItem('code-theme')
                    )
                );
            }
            if (localStorage.getItem('code')) {
                changeLangauge(
                    //@ts-ignore
                    localStorage.getItem('code')
                );
            }

            setIsloading(false);
        } catch (err) {
            setIsloading(false);
        }
    }, [solution_link, content]);

    return (
        <Dialog>
            <DialogTrigger asChild>
                <Button variant="default" onClick={fetchCode}>
                    See code
                </Button>
            </DialogTrigger>
            <DialogContent className="sm:max-w-full overflow-y-auto">
                <DialogHeader>
                    <div className="flex items-center justify-start gap-3">
                        <ThemeDropdown
                            //@ts-ignore
                            setCodetheme={setCodetheme}
                        />
                        <CodeDropDown
                            setCode={changeLangauge}
                            fetchCode={fetchCode}
                        />
                    </div>
                </DialogHeader>
                {isloading ? (
                    <LoadingSpinner name="solution" />
                ) : (
                    <SyntaxHighlighter
                        language={
                            localStorage.getItem('code')
                                ? localStorage.getItem('code')
                                : 'python'
                        }
                        style={codetheme}
                    >
                        {content.codeTxt}
                    </SyntaxHighlighter>
                )}
            </DialogContent>
        </Dialog>
    );
};

export default React.memo(CodeSolution);
// export default CodeSolution;
