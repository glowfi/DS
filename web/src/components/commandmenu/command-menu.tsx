'use client';

import { DialogProps } from '@radix-ui/react-dialog';
import React from 'react';
import { cn, getColor, searchInListOfLists } from '../../lib/utils';
import {
    CommandDialog,
    CommandEmpty,
    CommandGroup,
    CommandItem,
    CommandList
} from '../ui/command';

import { SquareArrowOutUpRight } from 'lucide-react';
import Link from 'next/link';
import LoadingSpinner from '../loadingspinners/loadingspinner';
import CodeSolution from '../topics/code-solution';
import { data_location } from '../topics/constants';
import { Badge } from '../ui/badge';
import { Button } from '../ui/button';
import { Input } from '../ui/input';
import { useDebounce } from './hooks/useDebounce';

const CommandMenu = ({ ...props }: DialogProps) => {
    const [open, setOpen] = React.useState(false);
    const [searchTerm, setSearchTerm] = React.useState<string>('');
    const [debouncedText, isloadingtxt, setIsloadingtxt] =
        useDebounce(searchTerm);

    const [isloading, setIsloading] = React.useState(true);
    const [data, setData] = React.useState<any[]>([]);
    const [showData, setShowData] = React.useState<any[]>([]);

    React.useEffect(() => {
        console.log('Initial Render!');
        const fetchData = async () => {
            try {
                const data = await fetch(data_location);
                const json = await data.json();
                setData(() => [...Object.values(json).flat()]);
                setIsloading(false);
            } catch (err) {
                setIsloading(false);
            }
        };

        fetchData();
    }, []);

    React.useEffect(() => {
        if (data) {
            const newData = searchInListOfLists(data, debouncedText);
            console.log(newData);
            setShowData(() => [...JSON.parse(JSON.stringify(newData))]);
        }
    }, [debouncedText, data]);

    React.useEffect(() => {
        const down = (e: KeyboardEvent) => {
            if ((e.key === 'k' && (e.metaKey || e.ctrlKey)) || e.key === '/') {
                e.preventDefault();
                setOpen((open) => !open);
            }
        };

        document.addEventListener('keydown', down);
        return () => document.removeEventListener('keydown', down);
    }, []);

    if (isloading) {
        return <LoadingSpinner name="data" />;
    }

    return (
        <>
            <Button
                variant="outline"
                className={cn(
                    'relative h-8 justify-center rounded-[0.5rem] bg-background text-sm font-normal text-muted-foreground shadow-none sm:pr-12 w-full text-center'
                )}
                onClick={() => setOpen(true)}
                {...props}
            >
                <span className="hidden lg:inline-flex">Search codes...</span>
                <span className="inline-flex lg:hidden">Search codes...</span>
                <kbd className="pointer-events-none absolute right-[0.3rem] top-[0.3rem] hidden h-5 select-none items-center gap-1 rounded border bg-muted px-1.5 font-mono text-[10px] font-medium opacity-100 sm:flex">
                    <span className="text-xs">⌘</span>K
                </kbd>
            </Button>
            <CommandDialog open={open} onOpenChange={setOpen}>
                <Input
                    placeholder="Type a command or search..."
                    value={searchTerm}
                    className="focus-visible:ring-0"
                    onChange={(e) => {
                        // @ts-ignore
                        setSearchTerm(e?.target?.value);
                    }}
                />
                <CommandList>
                    <CommandEmpty>No results found.</CommandEmpty>

                    {isloadingtxt ? (
                        <LoadingSpinner name="results" />
                    ) : (
                        <CommandGroup heading="Codes">
                            {showData.map(
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
                                        <CommandItem
                                            className="w-full"
                                            key={idx}
                                        >
                                            <div className="flex items-center gap-1 justify-between w-full">
                                                <Link
                                                    target="_blank"
                                                    href={problem_link}
                                                    className="font-bold flex-col gap-1 hover:underline"
                                                >
                                                    {problem_name}
                                                    <SquareArrowOutUpRight className="h-4 w-4" />
                                                </Link>
                                                <div className="flex items-start justify-start gap-1 m-1">
                                                    <Badge>{topic}</Badge>
                                                    <Badge
                                                        style={{
                                                            backgroundColor: `${getColor(difficulty)}`
                                                        }}
                                                    >
                                                        {difficulty}
                                                    </Badge>
                                                </div>
                                                <CodeSolution
                                                    solution_link={
                                                        solution_link
                                                    }
                                                    problem_name={problem_name}
                                                />
                                            </div>
                                        </CommandItem>
                                    );
                                }
                            )}
                        </CommandGroup>
                    )}
                </CommandList>
            </CommandDialog>
        </>
    );
};

export default React.memo(CommandMenu);
// export default CommandMenu;
