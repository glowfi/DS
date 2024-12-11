'use client';
import {
    CommandDialog,
    CommandEmpty,
    CommandGroup,
    CommandInput,
    CommandItem,
    CommandList
} from '@/components/ui/command';
import { Question } from '@/lib/types';
import React, { useEffect, useState } from 'react';
import { Input } from './ui/input';
import { getColor, getLangaugeFromLocalStorage } from './topics';
import { Badge } from './ui/badge';
import Link from 'next/link';
import { SquareArrowOutUpRight } from 'lucide-react';

interface SearchBarProps {
    data: Question[];
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

const SearchBar: React.FunctionComponent<SearchBarProps> = ({ data }) => {
    const [open, setOpen] = React.useState(false);
    const [searchTerm, setSearchTerm] = useState('');
    const debouncedSearchTerm = useDebouncedValue(searchTerm, 500);
    const [filteredData, setFilteredData] = useState<Question[]>([]);

    useEffect(() => {
        setFilteredData(
            searchTerm === ''
                ? []
                : data.filter(
                      (d) =>
                          JSON.stringify(d)
                              .toLowerCase()
                              .includes(searchTerm.toLowerCase()) &&
                          d.language === getLangaugeFromLocalStorage()
                  )
        );
    }, [debouncedSearchTerm]);

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
                className="text-sm text-muted-foreground hover:opacity-70 hover:cursor-pointer"
                onClick={() => {
                    setOpen(true);
                }}
            >
                Press to start searching{' '}
                <kbd className="pointer-events-none inline-flex h-5 select-none items-center gap-1 rounded border bg-muted px-1.5 font-mono text-[10px] font-medium text-muted-foreground opacity-100">
                    <span className="text-xs">⌘</span>K
                </kbd>
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
                        {filteredData.map((d, idx) => {
                            return (
                                <CommandItem key={idx}>
                                    <div className="flex justify-between items-start w-full">
                                        <Link
                                            target="_blank"
                                            href={d.problem_link}
                                            className="font-bold flex-col gap-1 hover:underline"
                                        >
                                            {d.problem_name}
                                            <SquareArrowOutUpRight className="h-4 w-4" />
                                        </Link>
                                        <div className="flex items-start justify-start gap-1 m-1 w-fit">
                                            <Badge className="text-center">
                                                {d.topic}
                                            </Badge>
                                            <Badge
                                                style={{
                                                    backgroundColor: `${getColor(d.difficulty)}`
                                                }}
                                            >
                                                {d.difficulty}
                                            </Badge>
                                        </div>
                                        <Link
                                            target="_blank"
                                            href={d.solution_link}
                                            className="font-bold flex-col gap-1 hover:underline"
                                        >
                                            Solution
                                            <SquareArrowOutUpRight className="h-4 w-4" />
                                        </Link>
                                    </div>
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
