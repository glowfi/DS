import React from 'react';
import Topics from '../components/topics/topics';
import { data_location } from '../components/topics/constants';
import { Question } from '../lib/types';

const Page = async () => {
    const data = await fetch(data_location);
    const json: Question[] = await data.json();
    const topics: string[] = Object.keys(json);

    return (
        <div className="container mt-6 w-full h-dvh flex justify-center items-start">
            <Topics data={json} topics={topics} />
        </div>
    );
};

export default Page;
