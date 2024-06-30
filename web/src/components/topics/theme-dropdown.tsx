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
import { THEME, _THEME } from './code-themes';

export function ThemeDropdown({ setCodetheme }: any) {
    const [position, setPosition] = React.useState('bottom');
    let currTheme = localStorage.getItem('code-theme')
        ? localStorage.getItem('code-theme')
        : 'gruvboxDark';

    return (
        <DropdownMenu modal={false}>
            <DropdownMenuTrigger asChild>
                <Button variant="outline">Theme</Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent className="w-56">
                {/* @ts-ignore */}
                <DropdownMenuGroup value={position} onValueChange={setPosition}>
                    <ScrollArea className="h-72 w-full rounded-md">
                        {THEME.map((theme, idx) => {
                            return (
                                <DropdownMenuItem
                                    className={`${theme === currTheme ? 'bg-muted' : ''}`}
                                    /* @ts-ignore */
                                    value={theme}
                                    key={idx}
                                    onClick={() => {
                                        localStorage.setItem(
                                            'code-theme',
                                            THEME[idx]
                                        );
                                        setCodetheme(_THEME[idx]);
                                    }}
                                >
                                    {theme}
                                </DropdownMenuItem>
                            );
                        })}
                    </ScrollArea>
                </DropdownMenuGroup>
            </DropdownMenuContent>
        </DropdownMenu>
    );
}
