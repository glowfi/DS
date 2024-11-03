'use client';

import React from 'react';
import LoadingSpinner from '../loadingspinners/loadingspinner';
import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger
} from '../ui/accordion';
import { Badge } from '../ui/badge';
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
                            <AccordionTrigger>
                                <div className="flex gap-3 justify-between items-center">
                                    {topic}
                                    <Badge variant="default">
                                        {data[topic] ? data[topic].length : 0}
                                    </Badge>
                                </div>
                            </AccordionTrigger>
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
