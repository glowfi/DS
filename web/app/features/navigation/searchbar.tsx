'use client';
import { Question } from '@/app/lib/types';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import {
    CommandDialog,
    CommandEmpty,
    CommandGroup,
    CommandItem,
    CommandList
} from '@/components/ui/command';
import { Input } from '@/components/ui/input';
import { SquareArrowOutUpRight } from 'lucide-react';
import Link from 'next/link';
import React, { useEffect, useState } from 'react';
import { getColor } from '../topics/topics';

interface SearchBarProps {
    questions: Question[];
    onSeeCode: (question: Question) => void;
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
    questions,
    onSeeCode
}) => {
    const [isOpen, setIsOpen] = React.useState(false);
    const [searchQuery, setSearchQuery] = useState('');
    const debouncedSearchQuery = useDebouncedValue(searchQuery, 500);
    const [filteredQuestions, setFilteredQuestions] = useState<Question[]>([]);

    useEffect(() => {
        if (questions) {
            setFilteredQuestions(
                searchQuery === ''
                    ? []
                    : questions.filter((question) =>
                          JSON.stringify(question)
                              .toLowerCase()
                              .includes(searchQuery.toLowerCase())
                      )
            );
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [debouncedSearchQuery, questions]);

    React.useEffect(() => {
        const handleKeyDown = (event: KeyboardEvent) => {
            if (event.key === 'k' && (event.metaKey || event.ctrlKey)) {
                event.preventDefault();
                setIsOpen((prevIsOpen) => !prevIsOpen);
            }
        };
        document.addEventListener('keydown', handleKeyDown);
        return () => document.removeEventListener('keydown', handleKeyDown);
    }, []);

    return (
        <div className="w-full max-w-3xl mx-auto p-4">
            <div className="flex justify-center md:justify-start mb-1">
                <p
                    className="text-sm text-muted-foreground hover:opacity-70 hover:cursor-pointer md:hidden"
                    onClick={() => setIsOpen(true)}
                >
                    Search
                </p>
                <p
                    className="hidden md:block text-sm text-muted-foreground hover:opacity-70 hover:cursor-pointer"
                    onClick={() => setIsOpen(true)}
                >
                    Press to start searching{' '}
                    <kbd className="pointer-events-none inline-flex h-5 select-none items-center gap-1 rounded border bg-muted px-1.5 font-mono text-[10px] font-medium text-muted-foreground opacity-100">
                        <span className="text-xs">⌘</span>K
                    </kbd>
                </p>
            </div>
            <CommandDialog open={isOpen} onOpenChange={setIsOpen}>
                <Input
                    placeholder="Search questions..."
                    value={searchQuery}
                    className="focus-visible:ring-0 w-full"
                    onChange={(event) => setSearchQuery(event.target.value)}
                />
                <CommandList className="max-h-96 overflow-y-auto">
                    <CommandEmpty>No results found.</CommandEmpty>
                    <CommandGroup heading="Suggestions">
                        {filteredQuestions &&
                            filteredQuestions.length > 0 &&
                            filteredQuestions.map((question, index) => (
                                <CommandItem key={index} className="w-full">
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
                                        onClick={() => onSeeCode(question)}
                                        className="ml-auto"
                                    >
                                        See Code
                                    </Button>
                                </CommandItem>
                            ))}
                    </CommandGroup>
                </CommandList>
            </CommandDialog>
        </div>
    );
};

export default SearchBar;
