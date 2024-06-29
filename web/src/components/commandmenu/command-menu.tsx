'use client';

import * as React from 'react';

import {
    CommandDialog,
    CommandEmpty,
    CommandGroup,
    CommandInput,
    CommandItem,
    CommandList,
    CommandSeparator
} from '@/components/ui/command';
import { cn } from '@/lib/utils';
import { DialogProps } from '@radix-ui/react-dialog';

import { LaptopIcon, MoonIcon, SunIcon } from '@radix-ui/react-icons';
import { useTheme } from 'next-themes';
import { useRouter } from 'next/navigation';
import { Button } from '../ui/button';

export function CommandMenu({ ...props }: DialogProps) {
    const router = useRouter();
    const [open, setOpen] = React.useState(false);
    const { setTheme } = useTheme();

    React.useEffect(() => {
        const down = (e: KeyboardEvent) => {
            if ((e.key === 'k' && (e.metaKey || e.ctrlKey)) || e.key === '/') {
                if (
                    (e.target instanceof HTMLElement &&
                        e.target.isContentEditable) ||
                    e.target instanceof HTMLInputElement ||
                    e.target instanceof HTMLTextAreaElement ||
                    e.target instanceof HTMLSelectElement
                ) {
                    return;
                }

                e.preventDefault();
                setOpen((open) => !open);
            }
        };

        document.addEventListener('keydown', down);
        return () => document.removeEventListener('keydown', down);
    }, []);

    const runCommand = React.useCallback((command: () => unknown) => {
        setOpen(false);
        command();
    }, []);

    return (
        <div className="w-full">
            <Button
                variant="outline"
                className={cn(
                    'relative h-8 justify-center rounded-[0.5rem] bg-background text-sm font-normal text-muted-foreground shadow-none sm:pr-12 w-full text-center'
                )}
                onClick={() => setOpen(true)}
                {...props}
            >
                <span className="hidden lg:inline-flex text-center">
                    Search codes ...
                </span>
                <span className="inline-flex lg:hidden text-center">
                    Search codes...
                </span>
                <kbd className="pointer-events-none absolute right-[0.3rem] top-[0.3rem] hidden h-5 select-none items-center gap-1 rounded border bg-muted px-1.5 font-mono text-[10px] font-medium opacity-100 sm:flex">
                    <span className="text-xs">⌘</span>K
                </kbd>
            </Button>
            <CommandDialog open={open} onOpenChange={setOpen}>
                <CommandInput placeholder="Type a command or search..." />
                <CommandList>
                    <CommandEmpty>No results found.</CommandEmpty>
                    {/* <CommandGroup heading="Links"> */}
                    {/*   {docsConfig.mainNav */}
                    {/*     .filter((navitem) => !navitem.external) */}
                    {/*     .map((navItem) => ( */}
                    {/*       <CommandItem */}
                    {/*         key={navItem.href} */}
                    {/*         value={navItem.title} */}
                    {/*         onSelect={() => { */}
                    {/*           runCommand(() => router.push(navItem.href as string)) */}
                    {/*         }} */}
                    {/*       > */}
                    {/*         <FileIcon className="mr-2 h-4 w-4" /> */}
                    {/*         {navItem.title} */}
                    {/*       </CommandItem> */}
                    {/*     ))} */}
                    {/* </CommandGroup> */}
                    {/* {docsConfig.sidebarNav.map((group) => ( */}
                    {/*   <CommandGroup key={group.title} heading={group.title}> */}
                    {/*     {group.items.map((navItem) => ( */}
                    {/*       <CommandItem */}
                    {/*         key={navItem.href} */}
                    {/*         value={navItem.title} */}
                    {/*         onSelect={() => { */}
                    {/*           runCommand(() => router.push(navItem.href as string)) */}
                    {/*         }} */}
                    {/*       > */}
                    {/*         <div className="mr-2 flex h-4 w-4 items-center justify-center"> */}
                    {/*           <CircleIcon className="h-3 w-3" /> */}
                    {/*         </div> */}
                    {/*         {navItem.title} */}
                    {/*       </CommandItem> */}
                    {/*     ))} */}
                    {/*   </CommandGroup> */}
                    {/* ))} */}
                    <CommandSeparator />
                    <CommandGroup heading="Theme">
                        <CommandItem
                            onSelect={() => runCommand(() => setTheme('light'))}
                        >
                            <SunIcon className="mr-2 h-4 w-4" />
                            Light
                        </CommandItem>
                        <CommandItem
                            onSelect={() => runCommand(() => setTheme('dark'))}
                        >
                            <MoonIcon className="mr-2 h-4 w-4" />
                            Dark
                        </CommandItem>
                        <CommandItem
                            onSelect={() =>
                                runCommand(() => setTheme('system'))
                            }
                        >
                            <LaptopIcon className="mr-2 h-4 w-4" />
                            System
                        </CommandItem>
                    </CommandGroup>
                </CommandList>
            </CommandDialog>
        </div>
    );
}
