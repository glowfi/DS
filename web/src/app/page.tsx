import Topics from '@/components/topics';
import { dataLocation } from '@/lib/constants';
import { Question } from '@/lib/types';
import axios from 'axios';
import React from 'react';
import SiteHeader from '@/components/navbar';

const Home = async () => {
    const res = await axios.get(dataLocation);

    if (res.status !== 200) {
        return (
            <div className="container mt-6 w-full h-dvh flex justify-center items-center mx-auto">
                Error occured {res.statusText}
            </div>
        );
    }

    const json = res.data;
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
        <>
            <div className="container flex-col mt-6 w-full h-dvh flex justify-center items-center mx-auto">
                <SiteHeader data={json} />
                <Topics topics={Array.from(topics)} data={json} />
            </div>
        </>
    );
};

export default Home;
