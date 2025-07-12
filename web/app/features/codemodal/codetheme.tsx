'use client';

import { Check, ChevronsUpDown } from 'lucide-react';
import * as React from 'react';

import { Button } from '@/components/ui/button';
import {
    Command,
    CommandEmpty,
    CommandGroup,
    CommandInput,
    CommandItem
} from '@/components/ui/command';
import {
    Popover,
    PopoverContent,
    PopoverTrigger
} from '@/components/ui/popover';
import { ScrollArea } from '@/components/ui/scroll-area';
import { cn } from '@/lib/utils';
import { themes } from './codethemes';

interface CodeThemeSelectorProps {
    currentTheme: string;
    onThemeChange: (selTheme: string) => void;
}

const CodeThemeSelector: React.FunctionComponent<CodeThemeSelectorProps> = ({
    currentTheme,
    onThemeChange
}) => {
    const [open, setOpen] = React.useState(false);
    const [value, setValue] = React.useState(currentTheme);

    return (
        <Popover open={open} onOpenChange={setOpen} modal={true}>
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
                    <ChevronsUpDown className="ml-2 h-4 w-4 shrink-0 opacity-50" />
                </Button>
            </PopoverTrigger>
            <PopoverContent className="w-[200px] p-0">
                <Command>
                    <CommandInput placeholder="Search theme..." />
                    <CommandEmpty>No theme found.</CommandEmpty>
                    <CommandGroup>
                        <ScrollArea className="h-24">
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
                                            onThemeChange(currentValue);
                                        }
                                        setOpen(false);
                                    }}
                                >
                                    <Check
                                        className={cn(
                                            'mr-2 h-4 w-4',
                                            value === theme.value
                                                ? 'opacity-100'
                                                : 'opacity-0'
                                        )}
                                    />
                                    {theme.label}
                                </CommandItem>
                            ))}
                        </ScrollArea>
                    </CommandGroup>
                </Command>
            </PopoverContent>
        </Popover>
    );
};

export default CodeThemeSelector;
