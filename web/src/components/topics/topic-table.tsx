import { SquareArrowOutUpRight } from 'lucide-react';
import Link from 'next/link';
import React, { useState } from 'react';
import { DifficultyMap, getColor } from '../../lib/utils';
import { Badge } from '../ui/badge';
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow
} from '../ui/table';
import CodeSolution from './code-solution';
import { FaSort, FaSortDown, FaSortUp } from 'react-icons/fa';
import { Question } from '../../lib/types';

type theme = {
    [key: string]: React.CSSProperties;
};

type setTheme = React.Dispatch<
    React.SetStateAction<{
        [key: string]: React.CSSProperties;
    }>
>;

export interface Itheme {
    codetheme: theme;
    setCodetheme: setTheme;
}

interface sortOrder {
    order: string;
    icon: React.JSX.Element;
}

const ALLOWED_SORT_ORDER = {
    0: 'ORIG',
    1: 'ASC',
    2: 'DESC'
};

interface TopicTableProps {
    currTopic: string;
    data: Question[];
}

const TopicTable: React.FunctionComponent<TopicTableProps> = ({
    currTopic,
    data
}) => {
    const [currTopicData, setCurrTopicData] = useState(data);
    const [sortOrder, setSortOrder] = useState<sortOrder>({
        order: 'ASC',
        icon: <FaSort />
    });
    // @ts-ignore
    const [originalData, setOriginalData] = useState(
        structuredClone(data[currTopic])
    );

    // @ts-ignore
    function sortData(currData: Question[]) {
        let oldData = structuredClone(currData);

        if (
            sortOrder.order === ALLOWED_SORT_ORDER[1] ||
            sortOrder.order === ALLOWED_SORT_ORDER[2]
        ) {
            // @ts-ignore
            oldData.sort(function (a: Question, b: Question) {
                let a_difficulty = a.difficulty;
                let b_difficulty = b.difficulty;

                if (sortOrder.order == ALLOWED_SORT_ORDER[1]) {
                    setSortOrder(() => {
                        return {
                            order: ALLOWED_SORT_ORDER[2],
                            icon: <FaSortDown />
                        };
                    });
                    return (
                        // @ts-ignore
                        DifficultyMap[a_difficulty] -
                        // @ts-ignore
                        DifficultyMap[b_difficulty]
                    );
                } else if (sortOrder.order == ALLOWED_SORT_ORDER[2]) {
                    setSortOrder(() => {
                        return {
                            order: ALLOWED_SORT_ORDER[0],
                            icon: <FaSortUp />
                        };
                    });
                    return (
                        // @ts-ignore
                        DifficultyMap[b_difficulty] -
                        // @ts-ignore
                        DifficultyMap[a_difficulty]
                    );
                }
            });
        } else {
            setSortOrder(() => {
                return {
                    order: ALLOWED_SORT_ORDER[1],
                    icon: <FaSort />
                };
            });
            return originalData;
        }
        return oldData;
    }

    return (
        <Table>
            <TableHeader>
                <TableRow>
                    <TableHead>#</TableHead>
                    <TableHead>Problem</TableHead>
                    <TableHead
                        className="hover:cursor-pointer"
                        onClick={() => {
                            // @ts-ignore
                            setCurrTopicData((currData) => {
                                return sortData(currData);
                            });
                        }}
                    >
                        <div className="flex gap-3 justify-start items-center">
                            <p>Difficulty</p>
                            {sortOrder.icon}
                        </div>
                    </TableHead>
                    <TableHead>Code</TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                {currTopicData.map(
                    (
                        {
                            problem_name,
                            problem_link,
                            difficulty,
                            solution_link
                        },
                        idx: number
                    ) => {
                        return (
                            <TableRow key={idx}>
                                <TableCell>{idx}</TableCell>
                                <TableCell>
                                    <Link
                                        target="_blank"
                                        href={problem_link}
                                        className="hover:underline"
                                    >
                                        <div className="flex-row md:flex gap-2">
                                            {problem_name}
                                            <SquareArrowOutUpRight className="h-4 w-4" />
                                        </div>
                                    </Link>
                                </TableCell>
                                <TableCell>
                                    <Badge
                                        style={{
                                            backgroundColor: `${getColor(difficulty)}`
                                        }}
                                    >
                                        {difficulty}
                                    </Badge>
                                </TableCell>
                                <TableCell>
                                    <CodeSolution
                                        problem_name={problem_name}
                                        solution_link={solution_link}
                                    />
                                </TableCell>
                            </TableRow>
                        );
                    }
                )}
            </TableBody>
        </Table>
    );
};

// export default TopicTable;
export default React.memo(TopicTable);
