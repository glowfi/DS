'use client';

import Image from 'next/image';
import Link from 'next/link';
import React from 'react';
import Icon from '../app/icon.svg';
import { cn } from '@/lib/utils';
import { buttonVariants } from './ui/button';
import { ModeToggle } from './mode-toggle';
import { GitHubLogoIcon } from '@radix-ui/react-icons';
import { Question } from '@/lib/types';
import SearchBar from './searchbar';

interface SiteHeaderProps {
    data: Question[];
}

const SiteHeader: React.FunctionComponent<SiteHeaderProps> = ({ data }) => {
    return (
        <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
            <div className="container flex h-14 max-w-screen-2xl items-center">
                <div className="flex w-fit mr-2">
                    <Link href={'/'}>
                        <Image
                            src={Icon}
                            alt="Not Found"
                            width={35}
                            height={35}
                        />
                    </Link>
                </div>
                <div>
                    <Link
                        href="/"
                        className="mr-6 flex justify-center items-center space-x-2"
                    >
                        <span className="hidden md:inline-block font-bold">
                            {process.env.SITE_NAME}
                        </span>
                        <span className="md:hidden font-bold">
                            {process.env.SITE_NAME?.split(' ')
                                .map((w) => w.charAt(0))
                                .join('')
                                .replaceAll('&', '')}
                        </span>
                    </Link>
                </div>
                <div className="flex flex-1 items-center space-x-2 justify-end">
                    <nav className="flex items-center justify-center">
                        <SearchBar data={data} />
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
};

export default React.memo(SiteHeader);
