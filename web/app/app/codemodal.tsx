'use client';

import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import {
    Sheet,
    SheetClose,
    SheetContent,
    SheetFooter,
    SheetHeader,
    SheetTitle,
    SheetTrigger
} from '@/components/ui/sheet';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { SquareArrowOutUpRight } from 'lucide-react';
import Link from 'next/link';
import React, { useState } from 'react';
import SyntaxHighlighter from 'react-syntax-highlighter';
import { gruvboxDark } from 'react-syntax-highlighter/dist/esm/styles/hljs';
import CodeThemeSelector from './codetheme';
import { getThemeByValue, themes } from './codethemes';
import { Approach, Question } from './types';
import { getColor } from './topics';
import { Label } from '@/components/ui/label';

interface CodeModalProps {
    question: Question;
    modalOpen: boolean;
    onClose: () => void;
}

const mapApproachesToObject = (
    approaches: Approach[]
): Record<string, Approach> => {
    const seenTypes: Record<string, number> = {};

    return approaches.reduce(
        (acc, approach) => {
            if (seenTypes[approach.type]) {
                seenTypes[approach.type]++;
                acc[`${approach.type}_${seenTypes[approach.type]}`] = approach;
            } else {
                seenTypes[approach.type] = 1;
                acc[approach.type] = approach;
            }
            return acc;
        },
        {} as Record<string, Approach>
    );
};

const DEFAULT_THEME: {
    [key: string]: React.CSSProperties;
} = gruvboxDark;

function getThemeFromLocalStorage(): {
    [key: string]: React.CSSProperties;
} {
    const strTheme = localStorage.getItem('code-theme');
    if (strTheme === null || strTheme === undefined) {
        return DEFAULT_THEME;
    }
    const t = themes.find((t) => t.value === strTheme);
    if (t === undefined) {
        return DEFAULT_THEME;
    }

    return t.theme;
}
function setThemeToLocalStorage(theme: string): void {
    localStorage.setItem('code-theme', theme);
}

const CodeModal: React.FunctionComponent<CodeModalProps> = ({
    question,
    modalOpen,
    onClose
}) => {
    const [selectedApproach, setSelectedApproach] = useState(
        question.approaches[0].type
    );
    const [selectedTheme, setSelectedTheme] = useState(
        getThemeFromLocalStorage()
    );
    const approachesMap = mapApproachesToObject(question.approaches);
    console.log(approachesMap);

    const handleThemeChange = (selTheme: string) => {
        const theme = themes.find((t) => t.value === selTheme);
        if (theme) {
            setSelectedTheme(theme.theme);
            setThemeToLocalStorage(theme.value);
        }
    };

    return (
        <Sheet open={modalOpen} onOpenChange={onClose}>
            <SheetTrigger asChild className="hidden">
                <Button variant="outline">See Code</Button>
            </SheetTrigger>
            <SheetContent className="h-screen w-screen overflow-auto p-4 md:p-8">
                <SheetHeader>
                    <SheetTitle>
                        <Link
                            target="_blank"
                            href={question.problem_link}
                            className="hover:underline flex items-center gap-1"
                        >
                            <span>{question.problem_name}</span>
                            <SquareArrowOutUpRight className="h-4 w-4" />
                        </Link>
                    </SheetTitle>
                </SheetHeader>
                <div className="flex flex-col mt-6 overflow-auto gap-6">
                    <div className="flex flex-col gap-6">
                        <Badge
                            style={{
                                backgroundColor: `${getColor(question.difficulty)}`
                            }}
                        >
                            {question.difficulty}
                        </Badge>
                        <div className="flex flex-col gap-3">
                            <Label>Code Theme</Label>
                            <CodeThemeSelector
                                onThemeChange={handleThemeChange}
                                currentTheme={getThemeByValue(selectedTheme)}
                            />
                        </div>
                    </div>
                    <div className="flex flex-col gap-3">
                        <h3 className="text-2xl font-semibold tracking-tight">
                            Problem Statement
                        </h3>
                        <pre className="whitespace-pre-wrap">
                            {question.question}
                        </pre>
                    </div>

                    <div className="flex flex-col">
                        <h3 className="text-2xl font-semibold tracking-tight">
                            Intuition
                        </h3>
                        <pre className="whitespace-pre-wrap">
                            {approachesMap[selectedApproach].intuition}
                        </pre>
                    </div>

                    <Tabs defaultValue={selectedApproach}>
                        <TabsList className="gap-3">
                            {Object.keys(approachesMap).map((k, index) => {
                                return (
                                    <TabsTrigger
                                        value={`${k}`}
                                        key={index}
                                        onClick={() =>
                                            setSelectedApproach(
                                                approachesMap[k].type
                                            )
                                        }
                                    >
                                        {k}
                                    </TabsTrigger>
                                );
                            })}
                        </TabsList>

                        <div className="flex flex-col">
                            <h3 className="text-2xl font-semibold tracking-tight">
                                Approaches
                            </h3>
                            {Object.keys(approachesMap).map((k, index) => (
                                <TabsContent value={k} key={index}>
                                    <SyntaxHighlighter
                                        wrapLines={true}
                                        language={question.language}
                                        style={selectedTheme}
                                    >
                                        {approachesMap[k].code}
                                    </SyntaxHighlighter>
                                </TabsContent>
                            ))}
                        </div>

                        <div className="flex flex-col">
                            <h3 className="text-2xl font-semibold tracking-tight">
                                Time Complexity
                            </h3>
                            <Badge className="font-bold">
                                {approachesMap[selectedApproach].tc}
                            </Badge>
                        </div>
                        <div className="flex flex-col">
                            <h3 className="text-2xl font-semibold tracking-tight">
                                Space Complexity
                            </h3>
                            <Badge className="font-bold">
                                {approachesMap[selectedApproach].sc}
                            </Badge>
                        </div>
                    </Tabs>
                </div>
                <SheetFooter className="mt-3">
                    <SheetClose asChild>
                        <Button type="button" onClick={onClose}>
                            Close
                        </Button>
                    </SheetClose>
                </SheetFooter>
            </SheetContent>
        </Sheet>
    );
};

export default CodeModal;
