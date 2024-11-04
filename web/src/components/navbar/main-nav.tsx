'use client';

import Link from 'next/link';

export function MainNav() {
    return (
        <div className="mr-4 hidden md:flex">
            <Link
                href="/"
                className="mr-6 flex justify-center items-center space-x-2"
            >
                <span className="hidden font-bold sm:inline-block">
                    {process.env.SITE_NAME}
                </span>
            </Link>
        </div>
    );
}
