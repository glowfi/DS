import { SquareArrowOutUpRight } from 'lucide-react';
import Link from 'next/link';
import React from 'react';
import { getColor } from '../../lib/utils';
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

const TopicTable = ({ currTopic, data }: any) => {
    return (
        <Table>
            <TableHeader>
                <TableRow>
                    <TableHead>Problem</TableHead>
                    <TableHead>Difficulty</TableHead>
                    <TableHead>Code</TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                {data[currTopic].map(
                    (
                        [
                            id,
                            topic,
                            problem_name,
                            problem_link,
                            difficulty,
                            solution_link
                        ]: [
                            id: number,
                            topic: string,
                            problem_name: string,
                            problem_link: string,
                            difficulty: string,
                            solution_link: string
                        ],
                        idx: number
                    ) => {
                        return (
                            <TableRow key={idx}>
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
