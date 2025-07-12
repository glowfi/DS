'use client';
import {
    CommandDialog,
    CommandEmpty,
    CommandGroup,
    CommandItem,
    CommandList
} from '@/components/ui/command';
import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { SquareArrowOutUpRight } from 'lucide-react';
import { Question } from './types';
import { Input } from '@/components/ui/input';
import { getColor } from './topics';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';

interface SearchBarProps {
    data: Question[];
    handleSeeCode: (q: Question) => void;
}

const useDebouncedValue = (inputValue: string, delay: number) => {
    const [debouncedValue, setDebouncedValue] = useState(inputValue);

    useEffect(() => {
        const handler = setTimeout(() => {
            setDebouncedValue(inputValue);
        }, delay);

        return () => {
            clearTimeout(handler);
        };
    }, [inputValue, delay]);

    return debouncedValue;
};

const SearchBar: React.FunctionComponent<SearchBarProps> = ({
    data,
    handleSeeCode
}) => {
    const [open, setOpen] = React.useState(false);
    const [searchTerm, setSearchTerm] = useState('');
    const debouncedSearchTerm = useDebouncedValue(searchTerm, 500);
    const [filteredData, setFilteredData] = useState<Question[]>([]);

    useEffect(() => {
        setFilteredData(
            searchTerm === ''
                ? []
                : data.filter((d) =>
                      JSON.stringify(d)
                          .toLowerCase()
                          .includes(searchTerm.toLowerCase())
                  )
        );
    }, [debouncedSearchTerm, data]); // eslint-disable-line react-hooks/exhaustive-deps

    React.useEffect(() => {
        const down = (e: KeyboardEvent) => {
            if (e.key === 'k' && (e.metaKey || e.ctrlKey)) {
                e.preventDefault();
                setOpen((open) => !open);
            }
        };
        document.addEventListener('keydown', down);
        return () => document.removeEventListener('keydown', down);
    }, []);

    return (
        <>
            <p
                className="hidden md:block text-sm text-muted-foreground hover:opacity-70 hover:cursor-pointer"
                onClick={() => {
                    setOpen(true);
                }}
            >
                Press to start searching{' '}
                <kbd className="pointer-events-none inline-flex h-5 select-none items-center gap-1 rounded border bg-muted px-1.5 font-mono text-[10px] font-medium text-muted-foreground opacity-100">
                    <span className="text-xs">⌘</span>K
                </kbd>
            </p>
            <p
                className="md:hidden text-sm text-muted-foreground hover:opacity-70 hover:cursor-pointer"
                onClick={() => {
                    setOpen(true);
                }}
            >
                Click to start searching
            </p>
            <CommandDialog open={open} onOpenChange={setOpen}>
                <Input
                    placeholder="Type a command or search..."
                    value={searchTerm}
                    className="focus-visible:ring-0"
                    onChange={(e) => {
                        setSearchTerm(e.target.value);
                    }}
                />
                <CommandList>
                    <CommandEmpty>No results found.</CommandEmpty>
                    <CommandGroup heading="Suggestions">
                        {filteredData.map((question, idx) => {
                            return (
                                <CommandItem key={idx} className="w-full">
                                    <Link
                                        target="_blank"
                                        href={question.problem_link}
                                        className="font-bold flex-col hover:underline w-auto"
                                    >
                                        <span>{question.problem_name}</span>
                                        <SquareArrowOutUpRight className="h-4 w-4" />
                                    </Link>
                                    <div className="flex items-start justify-start gap-1 m-1 w-fit">
                                        <Badge className="text-center">
                                            {question.topic}
                                        </Badge>
                                        <Badge
                                            style={{
                                                backgroundColor: `${getColor(question.difficulty)}`
                                            }}
                                        >
                                            {question.difficulty}
                                        </Badge>
                                    </div>
                                    <Button
                                        onClick={() => {
                                            handleSeeCode(question);
                                        }}
                                    >
                                        See Code
                                    </Button>
                                </CommandItem>
                            );
                        })}
                    </CommandGroup>
                </CommandList>
            </CommandDialog>
        </>
    );
};

export default SearchBar;
