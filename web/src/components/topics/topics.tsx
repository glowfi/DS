'use client';
import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger
} from '@/components/ui/accordion';
import { useEffect, useState } from 'react';
import { data_location } from './constants';
import LoadingSpinner from '../loadingspinners/loadingspinner';

export function Topics() {
    const [isloading, setIsloading] = useState(true);
    const [topics, setTopics] = useState<string[]>([]);
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const data = await fetch(data_location);
                const json = await data.json();
                setTopics(Object.keys(json));
                setData(json);
                setIsloading(false);
            } catch (err) {
                console.log('Error Occured', err);
                setIsloading(false);
            }
        };
        fetchData();
    }, []);

    if (isloading) {
        return <LoadingSpinner name="codes" />;
    }

    return (
        <Accordion type="single" collapsible className="w-full">
            {topics.map((item: string, idx: number) => {
                return (
                    <AccordionItem value={`item-${idx + 1}`} key={idx}>
                        <AccordionTrigger>{item}</AccordionTrigger>
                        <AccordionContent>
                            Yes. It adheres to the WAI-ARIA design pattern.
                        </AccordionContent>
                    </AccordionItem>
                );
            })}
        </Accordion>
    );
}
