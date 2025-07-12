'use client';

import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Label } from '@/components/ui/label';
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
import CodeThemeSelector from './codetheme';
import {
    getThemeByValue,
    getThemeFromLocalStorage,
    setThemeToLocalStorage,
    themes
} from './codethemes';
import { Approach, Question } from '@/app/lib/types';
import { getColor } from '../topics/topics';

// Maps approaches to an object with unique keys
const mapApproachesToObject = (
    approaches: Approach[]
): Record<string, Approach> => {
    const seenTypes: Record<string, number> = {};

    return approaches.reduce(
        (acc, approach) => {
            if (seenTypes[approach.type]) {
                seenTypes[approach.type]++;
                acc[`${approach.type}-${seenTypes[approach.type]}`] = approach;
            } else {
                seenTypes[approach.type] = 1;
                acc[approach.type] = approach;
            }
            return acc;
        },
        {} as Record<string, Approach>
    );
};

interface CodeModalProps {
    question: Question;
    isModalOpen: boolean;
    onModalClose: () => void;
}

const CodeModal: React.FunctionComponent<CodeModalProps> = ({
    question,
    isModalOpen: modalOpen,
    onModalClose
}) => {
    const [selectedApproach, setSelectedApproach] = useState(
        question.approaches[0].type
    );
    const [selectedTheme, setSelectedTheme] = useState(
        getThemeFromLocalStorage()
    );
    const approachesMap = mapApproachesToObject(question.approaches);

    // Handle theme change and update local storage
    const handleThemeChange = (selTheme: string) => {
        const theme = themes.find((t) => t.value === selTheme);
        if (theme) {
            setSelectedTheme(theme.theme);
            setThemeToLocalStorage(theme.value);
        }
    };

    return (
        <Sheet open={modalOpen} onOpenChange={onModalClose}>
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
                                backgroundColor: getColor(question.difficulty)
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
                            {Object.keys(approachesMap).map((key, index) => (
                                <TabsTrigger
                                    value={key}
                                    key={index}
                                    onClick={() =>
                                        setSelectedApproach(
                                            approachesMap[key].type
                                        )
                                    }
                                >
                                    {key}
                                </TabsTrigger>
                            ))}
                        </TabsList>

                        <div className="flex flex-col">
                            <h3 className="text-2xl font-semibold tracking-tight">
                                Approaches
                            </h3>
                            {Object.keys(approachesMap).map((key, index) => (
                                <TabsContent value={key} key={index}>
                                    <SyntaxHighlighter
                                        wrapLines={true}
                                        language={question.language}
                                        style={selectedTheme}
                                    >
                                        {approachesMap[key].code}
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
                        <Button type="button" onClick={onModalClose}>
                            Close
                        </Button>
                    </SheetClose>
                </SheetFooter>
            </SheetContent>
        </Sheet>
    );
};

export default CodeModal;
