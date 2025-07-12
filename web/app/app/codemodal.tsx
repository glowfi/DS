'use client';

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
import { Approach, Question } from './types';
import { Badge } from '@/components/ui/badge';

interface CodeModalProps {
    question?: Question;
    modalOpen: boolean;
    onClose: () => void;
}

function approachesToObject(approaches: Approach[]): {
    [key: string]: Approach;
} {
    return approaches.reduce(
        (obj, approach) => ({ ...obj, [approach.type]: approach }),
        {}
    );
}

const CodeModal: React.FunctionComponent<CodeModalProps> = ({
    question,
    modalOpen,
    onClose
}) => {
    if (question === undefined) {
        return null;
    }

    const defaultSelectedAppraoch =
        question.approaches.length > 0 ? question.approaches[0].type : 'NA';
    const [selectedApproach, setSelectedApproach] = useState(
        defaultSelectedAppraoch
    );
    const appToObject = approachesToObject(question.approaches);

    return (
        <Sheet open={modalOpen} onOpenChange={onClose}>
            <SheetTrigger asChild className="hidden">
                <Button variant="outline">See Code</Button>
            </SheetTrigger>
            <SheetContent className="h-screen w-screen overflow-auto">
                <SheetHeader>
                    <SheetTitle>
                        <Link
                            target="_blank"
                            href={question.problem_link}
                            className="hover:underline"
                        >
                            <div className="flex-row items-center gap-1">
                                <span>{question.problem_name}</span>
                                <SquareArrowOutUpRight className="h-4 w-4" />
                            </div>
                        </Link>
                    </SheetTitle>
                </SheetHeader>
                <div className="flex flex-col mt-6 overflow-auto gap-6 justify-between">
                    <div className="flex flex-col">
                        <h3 className="scroll-m-20 text-2xl font-semibold tracking-tight">
                            Problem Statement
                        </h3>
                        <pre>{question.question}</pre>
                    </div>

                    <div className="flex flex-col">
                        <h3 className="scroll-m-20 text-2xl font-semibold tracking-tight">
                            Intuition
                        </h3>
                        <pre>{appToObject[selectedApproach].intuition}</pre>
                    </div>

                    <Tabs defaultValue={defaultSelectedAppraoch}>
                        <TabsList>
                            {question.approaches.map((a, idx) => {
                                return (
                                    <TabsTrigger
                                        value={`${a.type}-${idx}`}
                                        key={idx}
                                        onClick={() => {
                                            setSelectedApproach(a.type);
                                        }}
                                    >
                                        {a.type}
                                    </TabsTrigger>
                                );
                            })}
                        </TabsList>

                        <div className="flex flex-col">
                            <h3 className="scroll-m-20 text-2xl font-semibold tracking-tight">
                                Approaches
                            </h3>
                            {question.approaches.map((a, idx) => {
                                return (
                                    <TabsContent
                                        value={`${a.type}-${idx}`}
                                        key={idx}
                                    >
                                        <SyntaxHighlighter
                                            wrapLines={true}
                                            language={question.language}
                                            style={gruvboxDark}
                                        >
                                            {a.code}
                                        </SyntaxHighlighter>
                                    </TabsContent>
                                );
                            })}
                        </div>
                        <div className="flex flex-col">
                            <h3 className="scroll-m-20 text-2xl font-semibold tracking-tight">
                                Time Complexity
                            </h3>
                            <Badge>{appToObject[selectedApproach].tc}</Badge>
                        </div>
                        <div className="flex flex-col">
                            <h3 className="scroll-m-20 text-2xl font-semibold tracking-tight">
                                Space Complexity
                            </h3>
                            <Badge>{appToObject[selectedApproach].sc}</Badge>
                        </div>
                    </Tabs>
                </div>
                <SheetFooter className="mt-3">
                    <SheetClose asChild>
                        <Button type="submit" onClick={onClose}>
                            Close
                        </Button>
                    </SheetClose>
                </SheetFooter>
            </SheetContent>
        </Sheet>
    );
};

export default CodeModal;
