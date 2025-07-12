'use client';

import LoadingSpinner from '@/components/ui/loadingspinner';
import React, { useEffect, useState } from 'react';
import Navbar from './app/navbar';
import Topics from './app/topics';
import { Question } from './app/types';

const HomePage: React.FunctionComponent = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const [questions, setQuestions] = useState<Question[]>([]);

    const [isCodeModalOpen, setIsCodeModalOpen] = useState(false);
    const [currentSelectedQuestion, setCurrentSelectedQuestion] = useState<
        Question | undefined
    >();

    const openCodeModal = (question: Question) => {
        setIsCodeModalOpen(true);
        setCurrentSelectedQuestion(question);
    };

    const closeCodeModal = () => {
        setIsCodeModalOpen(false);
    };

    const fetchQuestions = async (url: string) => {
        setIsLoading(true);
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Failed to fetch: ${response.status}`);
            }
            const fetchedQuestions = (await response.json()) as Question[];
            setQuestions(fetchedQuestions);
        } catch (error) {
            const errorText =
                error instanceof Error
                    ? error.message
                    : 'An unexpected error occurred';
            setErrorMessage(errorText);
        } finally {
            setIsLoading(false);
        }
    };

    useEffect(() => {
        const dataUrl = process.env.NEXT_PUBLIC_DATA_LINK;
        if (dataUrl) {
            fetchQuestions(dataUrl);
        } else {
            setErrorMessage('Data source URL is not configured');
        }
    }, []);

    if (isLoading) {
        return (
            <div className="flex justify-center items-center h-dvh">
                <LoadingSpinner name="page" />
            </div>
        );
    }

    if (errorMessage) {
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
                    <p className="text-red-600 text-lg">{errorMessage}</p>
                </div>
            </div>
        );
    }

    return (
        <div className="container flex-col w-full h-dvh flex items-center mx-auto p-12 md:p-6">
            <Navbar questions={questions} onCodeView={openCodeModal} />
            <Topics
                questions={questions}
                modalOpen={isCodeModalOpen}
                selectedQuestion={currentSelectedQuestion}
                onModalClose={closeCodeModal}
                onCodeView={openCodeModal}
            />
        </div>
    );
};

export default HomePage;
