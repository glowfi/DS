import React from 'react';
import Topics from '../components/topics/topics';
import { data_location } from '../components/topics/constants';
import { Question } from '../lib/types';
import axios from 'axios';

const Page = async () => {
    const data = await axios.get(data_location);
    const json = data.data;
    const topics: Set<string> = json.reduce(
        (prev: Set<string>, currVal: Question) => {
            if (!prev.has(currVal.topic)) {
                prev.add(currVal.topic);
            }
            return prev;
        },
        new Set()
    );

    return (
        <div className="container mt-6 w-full h-dvh flex justify-center items-start">
            <Topics data={json} topics={Array.from(topics)} />
        </div>
    );
};

export default Page;
