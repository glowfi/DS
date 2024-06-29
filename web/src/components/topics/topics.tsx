'use client';

import React from 'react';
import LoadingSpinner from '../loadingspinners/loadingspinner';
import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger
} from '../ui/accordion';
import TopicTable from './topic-table';
import useFetch from './useFetch';

const Topics = () => {
    const { topics, setTopics, data, setData, isloading, setIsloading } =
        useFetch();

    if (isloading) {
        return <LoadingSpinner name="codes" />;
    }

    return (
        <div className="flex justify-center items-center w-full">
            <Accordion type="single" collapsible className="w-full">
                {topics.map((topic: string, idx: number) => {
                    return (
                        <AccordionItem value={`item-${idx + 1}`} key={idx}>
                            <AccordionTrigger>{topic}</AccordionTrigger>
                            <AccordionContent>
                                <TopicTable data={data} currTopic={topic} />
                            </AccordionContent>
                        </AccordionItem>
                    );
                })}
            </Accordion>
        </div>
    );
};

export default React.memo(Topics);
// export default Topics;
