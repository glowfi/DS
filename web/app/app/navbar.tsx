'use client';

import Image from 'next/image';
import Link from 'next/link';
import React from 'react';
import LogoIcon from '../icon.svg';
import { cn } from '@/lib/utils';
import { Question } from './types';
import { buttonVariants } from '@/components/ui/button';
import { ModeToggle } from './mode-toggle';
import { GitHubLogoIcon } from '@radix-ui/react-icons';
import SearchBar from './searchbar';

interface SiteHeaderProps {
    questions: Question[];
    onCodeView: (question: Question) => void;
}

const SiteHeader: React.FunctionComponent<SiteHeaderProps> = ({
    questions,
    onCodeView: onViewCode
}) => {
    return (
        <header className="sticky top-0 z-50 w-full border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
            <div className="container flex h-14 max-w-screen-2xl items-center">
                <LogoSection />
                <SiteTitle />
                <Navbar questions={questions} onViewCode={onViewCode} />
            </div>
        </header>
    );
};

const LogoSection = () => {
    return (
        <div className="flex w-fit mr-2">
            <Link href="/">
                <Image src={LogoIcon} alt="Site Logo" width={35} height={35} />
            </Link>
        </div>
    );
};

const SiteTitle = () => {
    return (
        <div>
            <Link
                href="/"
                className="mr-6 flex justify-center items-center space-x-2"
            >
                <span className="hidden md:inline-block font-bold">
                    {process.env.NEXT_PUBLIC_SITE_NAME}
                </span>
            </Link>
        </div>
    );
};

const GitHubLink = () => {
    return (
        <Link
            href={process.env.NEXT_PUBLIC_GITHUB_LINK as string}
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
    );
};

interface NavbarProps {
    questions: Question[];
    onViewCode: (question: Question) => void;
}

const Navbar: React.FunctionComponent<NavbarProps> = ({
    questions,
    onViewCode
}) => {
    return (
        <div className="flex flex-1 items-center space-x-2 justify-end">
            <nav className="flex items-center justify-center">
                <SearchBar questions={questions} onSeeCode={onViewCode} />
                <GitHubLink />
                <ModeToggle />
            </nav>
        </div>
    );
};

export default React.memo(SiteHeader);
