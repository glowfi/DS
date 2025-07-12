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

const mapApproachesToObject = (
    approaches: Approach[]
): Record<string, Approach> => {
    return approaches.reduce(
        (acc, approach) => {
            acc[approach.type] = approach;
            return acc;
        },
        {} as Record<string, Approach>
    );
};

const CodeModal: React.FC<CodeModalProps> = ({
    question,
    modalOpen,
    onClose
}) => {
    if (!question) {
        return null;
    }

    const defaultSelectedApproach =
        question.approaches.length > 0 ? question.approaches[0].type : 'NA';
    const [selectedApproach, setSelectedApproach] = useState(
        defaultSelectedApproach
    );
    const approachesMap = mapApproachesToObject(question.approaches);

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
                    <div className="flex flex-col">
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

                    <Tabs defaultValue={defaultSelectedApproach}>
                        <TabsList>
                            {question.approaches.map((approach, index) => (
                                <TabsTrigger
                                    value={`${approach.type}-${index}`}
                                    key={index}
                                    onClick={() =>
                                        setSelectedApproach(approach.type)
                                    }
                                >
                                    {approach.type}
                                </TabsTrigger>
                            ))}
                        </TabsList>

                        <div className="flex flex-col">
                            <h3 className="text-2xl font-semibold tracking-tight">
                                Approaches
                            </h3>
                            {question.approaches.map((approach, index) => (
                                <TabsContent
                                    value={`${approach.type}-${index}`}
                                    key={index}
                                >
                                    <SyntaxHighlighter
                                        wrapLines={true}
                                        language={question.language}
                                        style={gruvboxDark}
                                    >
                                        {approach.code}
                                    </SyntaxHighlighter>
                                </TabsContent>
                            ))}
                        </div>

                        <div className="flex flex-col">
                            <h3 className="text-2xl font-semibold tracking-tight">
                                Time Complexity
                            </h3>
                            <Badge>{approachesMap[selectedApproach].tc}</Badge>
                        </div>
                        <div className="flex flex-col">
                            <h3 className="text-2xl font-semibold tracking-tight">
                                Space Complexity
                            </h3>
                            <Badge>{approachesMap[selectedApproach].sc}</Badge>
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
