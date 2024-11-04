import React, { useState } from 'react';
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

const CodeSolution = ({
    solution_link,
    problem_name
}: {
    solution_link: string;
    problem_name: string;
}) => {
    const [content, setContent] = useState('');
    const [isloading, setIsloading] = useState(false);
    const { codetheme, setCodetheme } = useThemeCtx();

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
                            if (localStorage.getItem('code-theme')) {
                                setCodetheme(
                                    //@ts-ignore
                                    getThemeIndex(
                                        //@ts-ignore
                                        localStorage.getItem('code-theme')
                                    )
                                );
                            }

                            setIsloading(false);
                        } catch (err) {
                            setIsloading(false);
                        }
                    }}
                >
                    See code
                </Button>
            </DialogTrigger>
            <DialogContent className="overflow-y-auto">
                <DialogHeader>
                    <div className="flex items-center justify-center">
                        <ThemeDropdown
                            //@ts-ignore
                            setCodetheme={setCodetheme}
                        />
                    </div>
                </DialogHeader>
                {isloading ? (
                    <LoadingSpinner name="solution" />
                ) : (
                    <SyntaxHighlighter language="python" style={codetheme}>
                        {content}
                    </SyntaxHighlighter>
                )}
            </DialogContent>
        </Dialog>
    );
};

export default React.memo(CodeSolution);
// export default CodeSolution;
