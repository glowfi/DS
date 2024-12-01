'use client';

import React, { useState } from 'react';
import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger
} from '../ui/accordion';
import { Badge } from '../ui/badge';
import TopicTable from './topic-table';
import { Question } from '../../lib/types';

interface TopicsProps {
    topics: string[];
    data: Question[];
}

const Topics: React.FunctionComponent<TopicsProps> = ({ topics, data }) => {
    const [language, setLanguage] = useState<{ lang: string }>({
        lang: 'python'
    });

    function changeLangauge(language: string) {
        setLanguage((old) => ({ ...old, lang: language }));
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
                                        {
                                            data.filter(
                                                (p) =>
                                                    p.topic === topic &&
                                                    p.language === language.lang
                                            ).length
                                        }
                                    </Badge>
                                </div>
                            </AccordionTrigger>
                            <AccordionContent>
                                <TopicTable
                                    changeLangauge={changeLangauge}
                                    data={data.filter(
                                        (p) =>
                                            p.topic === topic &&
                                            p.language === language.lang
                                    )}
                                />
                            </AccordionContent>
                        </AccordionItem>
                    );
                })}
            </Accordion>
            <div className="flex justify-between items-center mt-3 mr-9">
                <h6 className="scroll-m-20  font-semibold tracking-tight">
                    Total Code(s)
                </h6>
                <Badge>
                    {data.filter((p) => p.language === language.lang).length}
                </Badge>
            </div>
        </div>
    );
};

export default React.memo(Topics);
// export default Topics;
