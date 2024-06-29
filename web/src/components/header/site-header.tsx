'use client';

import { cn } from '@/lib/utils';
import { GitHubLogoIcon } from '@radix-ui/react-icons';
import Link from 'next/link';
import { CommandMenu } from '../commandmenu/command-menu';
import { MainNav } from '../navbar/main-nav';
import { MobileNav } from '../navbar/mobile-nav';
import { ModeToggle } from '../themetoggle/mode-toggle';
import { buttonVariants } from '../ui/button';

export function SiteHeader() {
    return (
        <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
            <div className="flex h-14 max-w-screen-2xl items-center container">
                <MainNav />
                <MobileNav />
                <div className="flex items-center justify-between space-x-2 w-full">
                    <div className="w-full flex-1 md:flex-none overflow-hidden">
                        <CommandMenu />
                    </div>
                    <nav className="flex items-center">
                        <Link
                            href={process.env.GITHUB_LINK as string}
                            target="_blank"
                            rel="noreferrer"
                        >
                            <div
                                className={cn(
                                    buttonVariants({
                                        variant: 'ghost'
                                    }),
                                    'w-9 px-0'
                                )}
                            >
                                <GitHubLogoIcon className="h-4 w-4" />
                                <span className="sr-only">GitHub</span>
                            </div>
                        </Link>
                        <ModeToggle />
                    </nav>
                </div>
            </div>
        </header>
    );
}
