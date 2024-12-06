'use client';

import React from 'react';
import { Check, ChevronsUpDown } from 'lucide-react';

import { cn } from '@/lib/utils';
import { Button } from '@/components/ui/button';
import {
    Command,
    CommandEmpty,
    CommandGroup,
    CommandInput,
    CommandItem,
    CommandList
} from '@/components/ui/command';
import {
    Popover,
    PopoverContent,
    PopoverTrigger
} from '@/components/ui/popover';
import { allowedLanguages } from './codeLanguage';
import { Question } from '@/lib/types';

interface CodeLangauageProps {
    fetchCode: (solution_link: string) => Promise<void>;
    changeLangauge: (lang: string) => void;
    setLangaugeToLocalStorage(language: string): void;
    data: Question[];
    problem_name: string;
    language: string;
}

const CodeLangauage: React.FunctionComponent<CodeLangauageProps> = ({
    fetchCode,
    changeLangauge,
    setLangaugeToLocalStorage,
    data,
    problem_name,
    language
}) => {
    const [open, setOpen] = React.useState(false);
    const [value, setValue] = React.useState(language);

    return (
        <Popover open={open} onOpenChange={setOpen}>
            <PopoverTrigger asChild>
                <Button
                    variant="outline"
                    role="combobox"
                    aria-expanded={open}
                    className="w-[200px] justify-between"
                >
                    {value
                        ? allowedLanguages.find(
                              (language) => language.value === value
                          )?.label
                        : 'Select language...'}
                    <ChevronsUpDown className="ml-2 h-4 w-4 shrink-0 opacity-50" />
                </Button>
            </PopoverTrigger>
            <PopoverContent className="w-[200px] p-0">
                <Command>
                    <CommandInput placeholder="Search language..." />
                    <CommandList>
                        <CommandEmpty>No language found.</CommandEmpty>
                        <CommandGroup>
                            {allowedLanguages.map((language) => (
                                <CommandItem
                                    key={language.value}
                                    value={language.value}
                                    onSelect={async (currentValue) => {
                                        setValue(
                                            currentValue === value
                                                ? ''
                                                : currentValue
                                        );
                                        if (currentValue !== '') {
                                            const lang = allowedLanguages.find(
                                                (t) => t.value === currentValue
                                            );
                                            if (lang) {
                                                changeLangauge(language.value);
                                                const p = data.find(
                                                    (d) =>
                                                        d.language ===
                                                            lang.value &&
                                                        d.problem_name ===
                                                            problem_name
                                                );
                                                if (p) {
                                                    await fetchCode(
                                                        p.solution_link
                                                    );
                                                    // setLangaugeToLocalStorage(
                                                    //     language.value
                                                    // );
                                                }
                                            }
                                        }
                                        setOpen(false);
                                    }}
                                >
                                    <Check
                                        className={cn(
                                            'mr-2 h-4 w-4',
                                            value === language.value
                                                ? 'opacity-100'
                                                : 'opacity-0'
                                        )}
                                    />
                                    {language.label}
                                </CommandItem>
                            ))}
                        </CommandGroup>
                    </CommandList>
                </Command>
            </PopoverContent>
        </Popover>
    );
};

export default CodeLangauage;
