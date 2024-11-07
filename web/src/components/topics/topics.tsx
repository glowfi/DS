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
import { deFlatten } from '../../lib/utils';

const Topics = () => {
    const { topics, setTopics, data, setData, isloading, setIsloading } =
        useFetch();

    if (isloading) {
        return <LoadingSpinner name="codes" />;
    }

    return (
        <div className="flex-col justify-center items-center w-full mt-3">
            <Accordion type="single" collapsible className="w-full">
                {topics.map((topic: string, idx: number) => {
                    return (
                        <AccordionItem value={`item-${idx + 1}`} key={idx}>
                            <AccordionTrigger>
                                <div className="flex justify-between items-center w-full mr-6">
                                    <h6 className="scroll-m-20  font-semibold tracking-tight">
                                        {topic}
                                    </h6>
                                    <Badge variant="default">
                                        {/* @ts-ignore */}
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
            <div className="flex justify-between items-center mt-3 mr-9">
                <h6 className="scroll-m-20  font-semibold tracking-tight">
                    Total Code(s)
                </h6>
                <Badge>{deFlatten(data).length}</Badge>
            </div>
        </div>
    );
};

export default React.memo(Topics);
// export default Topics;
