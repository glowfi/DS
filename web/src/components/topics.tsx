'use client';

import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger
} from '@/components/ui/accordion';
import { Badge } from '@/components/ui/badge';
import {
    Sheet,
    SheetClose,
    SheetContent,
    SheetDescription,
    SheetFooter,
    SheetHeader,
    SheetTitle,
    SheetTrigger
} from '@/components/ui/sheet';
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow
} from '@/components/ui/table';
import { Question } from '@/lib/types';
import { AxiosError } from 'axios';
import { SquareArrowOutUpRight } from 'lucide-react';
import Link from 'next/link';
import React, { useCallback, useEffect, useState } from 'react';
import { FaSort, FaSortDown, FaSortUp } from 'react-icons/fa';
import SyntaxHighlighter from 'react-syntax-highlighter';
import { gruvboxDark } from 'react-syntax-highlighter/dist/esm/styles/hljs';
import CodeLangauage from './codeLangauge';
import CodeTheme from './codeTheme';
import { themes } from './codeThemes';
import LoadingSpinner from './loadingspinner';
import { Button } from './ui/button';

interface TopicsProps {
    topics: string[];
    data: Question[];
}

interface sortOrder {
    idx: number;
    order: string;
    icon: React.JSX.Element;
}

const sortOrders: sortOrder[] = [
    {
        idx: 0,
        order: 'ORIG',
        icon: <FaSort />
    },
    {
        idx: 1,
        order: 'ASC',
        icon: <FaSortDown />
    },
    {
        idx: 2,
        order: 'DESC',
        icon: <FaSortUp />
    }
];

export const getColor = (difficulty: string) => {
    if (difficulty === 'Easy') {
        return 'green';
    } else if (difficulty === 'Medium') {
        return '#999900';
    } else {
        return 'red';
    }
};

interface DifficultyMapType {
    [key: string]: number;
}

const DifficultyMap: DifficultyMapType = {
    Easy: 1,
    Medium: 2,
    Hard: 3
};

function sortData(
    data: Question[],
    topic: string,
    language: string,
    sortIdx: number
): Question[] {
    const filteredData = data.filter(
        (d) => d.topic === topic && d.language === language
    );

    const selectedTopicData = filteredData.filter((d) => d.topic === topic);
    const restData = filteredData.filter((d) => d.topic !== topic);

    if (sortIdx > 0 && selectedTopicData.length > 0) {
        selectedTopicData.sort(function (a, b) {
            const a_difficulty = DifficultyMap[a.difficulty];
            const b_difficulty = DifficultyMap[b.difficulty];

            if (sortIdx === 1) {
                return a_difficulty - b_difficulty;
            } else if (sortIdx === 2) {
                return b_difficulty - a_difficulty;
            }
            return 0;
        });
    }

    return [...selectedTopicData, ...restData];
}

export type theme = {
    [key: string]: React.CSSProperties;
};

const DEFAULT_LANG: string = 'python';
const DEFAULT_THEME: theme = gruvboxDark;
const DEFAULT_THEME_STR: string = 'gruvboxDark';

function getLangaugeFromLocalStorage(): string {
    const data = localStorage.getItem('code-lang');
    if (data === null || data === undefined) {
        return DEFAULT_LANG;
    }
    return data;
}
function setLangaugeToLocalStorage(language: string): void {
    localStorage.setItem('code-lang', language);
}

function getThemeFromLocalStorage(): theme {
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

const Topics: React.FunctionComponent<TopicsProps> = ({ topics, data }) => {
    const [state, setState] = useState<{
        data: Question[];
        theme: theme;
        language: string;
        sort: sortOrder;
        codeText: string;
        isLoading: boolean;
        error: string;
    }>({
        theme: DEFAULT_THEME,
        data,
        language: DEFAULT_LANG,
        sort: sortOrders[0],
        codeText: '',
        isLoading: false,
        error: ''
    });

    const fetchCode = useCallback(
        async (solution_link: string) => {
            setState({ ...state, isLoading: true });
            try {
                const text = await fetch(solution_link);
                const codeText = await text.text();
                setState({
                    ...state,
                    isLoading: false,
                    codeText,
                    error: ''
                });
            } catch (error) {
                const err = error as AxiosError;
                setState({
                    ...state,
                    isLoading: false,
                    error: 'Error occured : ' + err.toString()
                });
            }
        },
        [state]
    );

    function changeTheme(theme: theme) {
        setState((oldState) => ({ ...oldState, theme }));
    }
    function changeLangauge(lang: string) {
        setState((oldState) => ({ ...oldState, language: lang }));
    }

    const filteredData = useCallback(
        (topic: string): Question[] => {
            
            return sortData(
                state.data,
                topic,
                state.language,
                state.sort.idx
            ).filter((d) => d.topic === topic && d.language === state.language);
        },
        [state]
    );

    useEffect(() => {
        setState((oldState) => ({
            ...oldState,
            language: getLangaugeFromLocalStorage(),
            theme: getThemeFromLocalStorage()
        }));
    }, []);

    return (
        <Accordion
            type="single"
            collapsible
            className="flex-col justify-center items-center w-full h-full"
        >
            {topics.map((topic, idx) => {
                return (
                    <AccordionItem value={`item-${idx}`} key={idx}>
                        <AccordionTrigger>
                            <div className="flex justify-between items-center w-full mr-6">
                                <h6 className="scroll-m-20  font-semibold tracking-tight">
                                    {topic}
                                </h6>
                                <Badge>
                                    {
                                        data.filter(
                                            (d) =>
                                                d.topic === topic &&
                                                d.language === state.language
                                        ).length
                                    }
                                </Badge>
                            </div>
                        </AccordionTrigger>
                        <AccordionContent>
                            <Table>
                                <TableHeader>
                                    <TableRow>
                                        <TableHead>#</TableHead>
                                        <TableHead>Problem</TableHead>
                                        <TableHead
                                            className="hover:cursor-pointer"
                                            onClick={() => {
                                                setState((oldstate) => {
                                                    const n = sortOrders.length;
                                                    const newIdx =
                                                        (oldstate.sort.idx +
                                                            1) %
                                                        n;
                                                    return {
                                                        ...oldstate,
                                                        sort: sortOrders[newIdx]
                                                    };
                                                });
                                            }}
                                        >
                                            <div className="flex gap-3 justify-start items-center">
                                                <p>Difficulty</p>
                                                {state.sort.icon}
                                            </div>
                                        </TableHead>
                                        <TableHead>Solution</TableHead>
                                    </TableRow>
                                </TableHeader>
                                <TableBody>
                                    {filteredData(topic).map((d, idx) => {
                                        return (
                                            <TableRow key={idx}>
                                                <TableCell className="font-medium">
                                                    {idx + 1}
                                                </TableCell>
                                                <TableCell>
                                                    <Link
                                                        target="_blank"
                                                        href={d.problem_link}
                                                        className="hover:underline"
                                                    >
                                                        <div className="flex-wrap md:flex items-center gap-1">
                                                            <span>
                                                                {d.problem_name}
                                                            </span>
                                                            <SquareArrowOutUpRight className="h-4 w-4" />
                                                        </div>
                                                    </Link>
                                                </TableCell>
                                                <TableCell>
                                                    <Badge
                                                        style={{
                                                            backgroundColor: `${getColor(d.difficulty.trim())}`
                                                        }}
                                                    >
                                                        {d.difficulty}
                                                    </Badge>
                                                </TableCell>
                                                <TableCell>
                                                    <Sheet modal>
                                                        <SheetTrigger
                                                            onClick={async () => {
                                                                
                                                                await fetchCode(
                                                                    d.solution_link
                                                                );
                                                            }}
                                                            asChild
                                                        >
                                                            <Button variant="default">
                                                                See Code
                                                            </Button>
                                                        </SheetTrigger>
                                                        <SheetContent className="w-full overflow-auto">
                                                            <SheetHeader>
                                                                <SheetTitle>
                                                                    {
                                                                        d.problem_name
                                                                    }
                                                                </SheetTitle>
                                                                <SheetDescription>
                                                                    Code
                                                                    Solution
                                                                </SheetDescription>
                                                            </SheetHeader>
                                                            <div className="flex mt-3 gap-3">
                                                                <CodeTheme
                                                                    changeTheme={
                                                                        changeTheme
                                                                    }
                                                                    setThemeToLocalStorage={
                                                                        setThemeToLocalStorage
                                                                    }
                                                                    deafulttheme={
                                                                        themes.find(
                                                                            (
                                                                                t
                                                                            ) =>
                                                                                t.theme ===
                                                                                state.theme
                                                                        )
                                                                            ?.label ||
                                                                        DEFAULT_THEME_STR
                                                                    }
                                                                />
                                                                <CodeLangauage
                                                                    fetchCode={
                                                                        fetchCode
                                                                    }
                                                                    changeLangauge={
                                                                        changeLangauge
                                                                    }
                                                                    setLangaugeToLocalStorage={
                                                                        setLangaugeToLocalStorage
                                                                    }
                                                                    data={data}
                                                                    problem_name={
                                                                        d.problem_name
                                                                    }
                                                                    language={
                                                                        state.language
                                                                    }
                                                                />
                                                            </div>
                                                            <div className="grid gap-4 py-4">
                                                                {state.isLoading ? (
                                                                    <LoadingSpinner name="solution" />
                                                                ) : (
                                                                    <>
                                                                        {state
                                                                            .codeText
                                                                            .length >
                                                                            0 && (
                                                                            <SyntaxHighlighter
                                                                                language={
                                                                                    d.language
                                                                                }
                                                                                style={
                                                                                    state.theme
                                                                                }
                                                                            >
                                                                                {
                                                                                    state.codeText
                                                                                }
                                                                            </SyntaxHighlighter>
                                                                        )}
                                                                    </>
                                                                )}
                                                                {state.error
                                                                    .length >
                                                                    0 && (
                                                                    <div className="text-lg font-semibold text-red-500">
                                                                        {
                                                                            state.error
                                                                        }
                                                                    </div>
                                                                )}
                                                            </div>
                                                            <SheetFooter>
                                                                <SheetClose
                                                                    asChild
                                                                >
                                                                    <Button type="submit">
                                                                        Close
                                                                    </Button>
                                                                </SheetClose>
                                                            </SheetFooter>
                                                        </SheetContent>
                                                    </Sheet>
                                                </TableCell>
                                            </TableRow>
                                        );
                                    })}
                                </TableBody>
                            </Table>
                        </AccordionContent>
                    </AccordionItem>
                );
            })}
        </Accordion>
    );
};

export default Topics;
