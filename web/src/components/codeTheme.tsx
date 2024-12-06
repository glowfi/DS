'use client';

import { Check, ChevronsUpDown } from 'lucide-react';
import * as React from 'react';

import { cn } from '@/lib/utils';

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
import { themes } from './codeThemes';
import { theme } from './topics';
import { Button } from './ui/button';

interface CodeThemeProps {
    changeTheme(theme: theme): void;
    setThemeToLocalStorage(theme: string): void;
    deafulttheme: string;
}

const CodeTheme: React.FunctionComponent<CodeThemeProps> = ({
    changeTheme,
    setThemeToLocalStorage,
    deafulttheme
}) => {
    const [open, setOpen] = React.useState(false);
    const [value, setValue] = React.useState(deafulttheme);
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
                        ? themes.find((theme) => theme.value === value)?.label
                        : 'Select theme...'}
                    <ChevronsUpDown className="opacity-50" />
                </Button>
            </PopoverTrigger>
            <PopoverContent className="w-[200px] p-0">
                <Command>
                    <CommandInput placeholder="Search theme..." />
                    <CommandList>
                        <CommandEmpty>No theme found.</CommandEmpty>
                        <CommandGroup>
                            {themes.map((theme) => (
                                <CommandItem
                                    key={theme.value}
                                    value={theme.value}
                                    onSelect={(currentValue) => {
                                        setValue(
                                            currentValue === value
                                                ? ''
                                                : currentValue
                                        );
                                        if (currentValue !== '') {
                                            const theme = themes.find(
                                                (t) => t.value === currentValue
                                            );
                                            if (theme) {
                                                changeTheme(theme.theme);
                                                // setThemeToLocalStorage(
                                                //     theme.value
                                                // );
                                            }
                                        }
                                        setOpen(false);
                                    }}
                                >
                                    {theme.label}
                                    <Check
                                        className={cn(
                                            'ml-auto',
                                            value === theme.value
                                                ? 'opacity-100'
                                                : 'opacity-0'
                                        )}
                                    />
                                </CommandItem>
                            ))}
                        </CommandGroup>
                    </CommandList>
                </Command>
            </PopoverContent>
        </Popover>
    );
};

export default CodeTheme;
