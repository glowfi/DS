import * as React from 'react';
import { Button } from '../ui/button';
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuTrigger
} from '../ui/dropdown-menu';
import { ScrollArea } from '../ui/scroll-area';
import { languages } from './constants';

export function CodeDropDown({ setCode, fetchCode }: any) {
    const [position, setPosition] = React.useState('bottom');
    let currCode = localStorage.getItem('code')
        ? localStorage.getItem('code')
        : 'python';

    return (
        <DropdownMenu>
            <DropdownMenuTrigger asChild>
                <Button variant="outline">{currCode}</Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent className="w-56 h-fit">
                {/* @ts-ignore */}
                <DropdownMenuGroup value={position} onValueChange={setPosition}>
                    <ScrollArea className="h-fit w-full rounded-md">
                        {languages.map((lang, idx) => {
                            return (
                                <DropdownMenuItem
                                    className={`${lang === currCode ? 'bg-muted' : ''}`}
                                    /* @ts-ignore */
                                    value={lang}
                                    key={idx}
                                    onClick={() => {
                                        localStorage.setItem('code', lang);
                                        setCode(lang);
                                        fetchCode();
                                    }}
                                >
                                    {lang}
                                </DropdownMenuItem>
                            );
                        })}
                    </ScrollArea>
                </DropdownMenuGroup>
            </DropdownMenuContent>
        </DropdownMenu>
    );
}
