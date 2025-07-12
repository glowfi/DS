'use client';

import LoadingSpinner from '@/components/ui/loadingspinner';
import { useEffect, useState } from 'react';
import Topics from './app/topics';
import { Question } from './app/types';
import Navbar from './app/navbar';

export default function Home() {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [data, setData] = useState<Question[]>([]);

    const [modalOpen, setModalOpen] = useState<boolean>(false);
    const [selectedQuestion, setSelectedQuestion] = useState<Question>();

    const handleSeeCode = (q: Question) => {
        setModalOpen(true);
        setSelectedQuestion(q);
    };

    const handleCloseModal = (): void => {
        setModalOpen(false);
    };

    const fetchData = async (url: string) => {
        setLoading(true);
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }
            const json = await response.json();
            setData(json as Question[]);
        } catch (error: unknown) {
            // Type guard to check if error is an Error instance
            if (error instanceof Error) {
                setError(error.message);
            } else {
                // Fallback for unexpected error types
                setError('An unknown error occurred');
            }
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        const url = process.env.NEXT_PUBLIC_DATA_LINK;
        if (url) {
            fetchData(url);
        } else {
            setError('NEXT_PUBLIC_DATA_LINK is not defined');
        }
    }, []);

    if (loading) {
        return (
            <div className="flex justify-center items-center h-dvh">
                <LoadingSpinner name="page" />
            </div>
        );
    }

    if (error) {
        return (
            <div className="flex justify-center items-center h-dvh bg-red-100 p-4 rounded-lg shadow-lg">
                <div className="flex items-center gap-2">
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-6 w-6 text-red-600"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        strokeWidth={2}
                    >
                        <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                        />
                    </svg>
                    <p className="text-red-600 text-lg">{error}</p>
                </div>
            </div>
        );
    }

    return (
        <div className="container flex-col w-full h-dvh flex items-center mx-auto p-12 md:p-6">
            <Navbar questions={data} onSeeCode={handleSeeCode} />
            <Topics
                questions={data}
                modalOpen={modalOpen}
                selectedQuestion={selectedQuestion}
                onModalClose={handleCloseModal}
                onSeeCode={handleSeeCode}
            />
        </div>
    );
}
