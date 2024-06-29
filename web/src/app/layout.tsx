import type { Metadata } from 'next';
import './globals.css';
import { ThemeProvider } from '@/components/themetoggle/theme-provider';
import { SiteHeader } from '@/components/header/site-header';

export const metadata: Metadata = {
    title: 'Data structures and algorithms',
    description: 'DSA sheet'
};

export default function RootLayout({
    children
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en">
            <body>
                <ThemeProvider
                    attribute="class"
                    defaultTheme="system"
                    enableSystem
                    disableTransitionOnChange
                >
                    <SiteHeader />
                    {children}
                </ThemeProvider>
            </body>
        </html>
    );
}
