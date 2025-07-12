import { Difficulty, Question } from '@/app/lib/types';
import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger
} from '@/components/ui/accordion';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow
} from '@/components/ui/table';
import { SquareArrowOutUpRight } from 'lucide-react';
import Link from 'next/link';
import React, { useState } from 'react';
import { FaSort, FaSortDown, FaSortUp } from 'react-icons/fa';
import CodeModal from '../codemodal/codemodal';

export const getColor = (difficulty: string) => {
    if (difficulty === 'Easy') {
        return 'green';
    } else if (difficulty === 'Medium') {
        return '#999900';
    } else {
        return 'red';
    }
};

interface sortOrder {
    idx: number;
    order: string;
    icon: React.JSX.Element;
    compare: (a: Question, b: Question) => number;
}

const sortOrders: sortOrder[] = [
    {
        idx: 0,
        order: 'ORIGINAL',
        icon: <FaSort />,
        compare: () => 0
    },
    {
        idx: 1,
        order: 'ASCENDING',
        icon: <FaSortDown />,
        compare: (a, b) => {
            const difficultyOrder = {
                [Difficulty.Easy]: 0,
                [Difficulty.Medium]: 1,
                [Difficulty.Hard]: 2
            };
            return (
                difficultyOrder[a.difficulty] - difficultyOrder[b.difficulty]
            );
        }
    },
    {
        idx: 2,
        order: 'DESCENDING',
        icon: <FaSortUp />,
        compare: (a, b) => {
            const difficultyOrder = {
                [Difficulty.Easy]: 0,
                [Difficulty.Medium]: 1,
                [Difficulty.Hard]: 2
            };
            return (
                difficultyOrder[b.difficulty] - difficultyOrder[a.difficulty]
            );
        }
    }
];

function sortQuestionsByDifficulty(
    questions: Question[],
    currSortOrderIdx: number
): Question[] {
    return questions.sort(sortOrders[currSortOrderIdx].compare);
}

function getTopicWiseQuestions(questions: Question[]): {
    [topic: string]: Question[];
} {
    const topicWiseQuestions: { [topic: string]: Question[] } = {};

    questions.forEach((question) => {
        if (!topicWiseQuestions[question.topic]) {
            topicWiseQuestions[question.topic] = [];
        }
        topicWiseQuestions[question.topic].push(question);
    });

    return topicWiseQuestions;
}

function getAllTopics(questions: Question[]): string[] {
    const topics: Set<string> = new Set();

    questions.forEach((question) => {
        topics.add(question.topic);
    });

    return Array.from(topics);
}

function getSortedQuestionsByTopic(
    questions: Question[],
    currSortOrderIdx: number
): { [topic: string]: Question[] } {
    const topicWiseQuestions = getTopicWiseQuestions(questions);
    const sortedTopicWiseQuestions: { [topic: string]: Question[] } = {};

    Object.keys(topicWiseQuestions).forEach((topic) => {
        sortedTopicWiseQuestions[topic] = sortQuestionsByDifficulty(
            topicWiseQuestions[topic],
            currSortOrderIdx
        );
    });

    return sortedTopicWiseQuestions;
}

interface TopicsProps {
    questions: Question[];
    selectedQuestion?: Question;
    modalOpen: boolean;
    onCodeView: (q: Question) => void;
    onModalClose: () => void;
}

const Topics: React.FunctionComponent<TopicsProps> = ({
    questions,
    selectedQuestion,
    modalOpen,
    onCodeView,
    onModalClose
}) => {
    const [sortOrder, setSortOrder] = useState<number>(0);

    const topics = getAllTopics(questions);
    const topicWiseQuestions = getSortedQuestionsByTopic(questions, sortOrder);

    const cycleSortOrder = () => {
        setSortOrder((oldstate) => {
            const n = sortOrders.length;
            const newIdx = (oldstate + 1) % n;
            return newIdx;
        });
    };

    return (
        <React.Fragment>
            <Accordion
                type="single"
                collapsible
                className="flex-col justify-center items-center w-full h-full"
            >
                {topics.map((topic, idx1) => {
                    return (
                        <AccordionItem value={`item-${idx1}`} key={idx1}>
                            <AccordionTrigger>
                                <div className="flex justify-between items-center w-full mr-6">
                                    <h6 className="scroll-m-20  font-semibold tracking-tight">
                                        {topic}
                                    </h6>
                                    <Badge>
                                        {topicWiseQuestions[topic].length}
                                    </Badge>
                                </div>
                            </AccordionTrigger>
                            <AccordionContent className="flex flex-col gap-4 text-balance">
                                <Table>
                                    <TableHeader>
                                        <TableRow>
                                            <TableHead>#</TableHead>
                                            <TableHead>Problem</TableHead>
                                            <TableHead
                                                className="hover:cursor-pointer"
                                                onClick={cycleSortOrder}
                                            >
                                                <div className="flex gap-3 justify-start items-center">
                                                    <p>Difficulty</p>
                                                    {sortOrders[sortOrder].icon}
                                                </div>
                                            </TableHead>
                                            <TableHead>Solution</TableHead>
                                        </TableRow>
                                    </TableHeader>
                                    <TableBody>
                                        {topicWiseQuestions[topic].map(
                                            (q, idx2) => {
                                                return (
                                                    <TableRow key={idx2}>
                                                        <TableCell className="font-medium">
                                                            {idx2 + 1}
                                                        </TableCell>
                                                        <TableCell>
                                                            <Link
                                                                target="_blank"
                                                                href={
                                                                    q.problem_link
                                                                }
                                                                className="hover:underline"
                                                            >
                                                                <div className="flex-wrap md:flex items-center gap-1">
                                                                    <span>
                                                                        {
                                                                            q.problem_name
                                                                        }
                                                                    </span>
                                                                    <SquareArrowOutUpRight className="h-4 w-4" />
                                                                </div>
                                                            </Link>
                                                        </TableCell>
                                                        <TableCell>
                                                            <Badge
                                                                style={{
                                                                    backgroundColor: `${getColor(q.difficulty.trim())}`
                                                                }}
                                                            >
                                                                {q.difficulty}
                                                            </Badge>
                                                        </TableCell>
                                                        <TableCell>
                                                            <Button
                                                                onClick={() => {
                                                                    onCodeView(
                                                                        q
                                                                    );
                                                                }}
                                                            >
                                                                See Code
                                                            </Button>
                                                        </TableCell>
                                                    </TableRow>
                                                );
                                            }
                                        )}
                                    </TableBody>
                                </Table>
                            </AccordionContent>
                        </AccordionItem>
                    );
                })}
                <div className="flex justify-between items-center mt-3 mr-13">
                    <h6 className="scroll-m-20  font-semibold tracking-tight">
                        Total Code(s)
                    </h6>
                    <Badge>{questions.length}</Badge>
                </div>
            </Accordion>
            {selectedQuestion !== undefined && (
                <CodeModal
                    question={selectedQuestion}
                    isModalOpen={modalOpen}
                    onModalClose={onModalClose}
                />
            )}
        </React.Fragment>
    );
};

export default Topics;
