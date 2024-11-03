'use client';

import React, { useEffect, useState } from 'react';
import { data_location } from './constants';

const useFetch = () => {
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
                setIsloading(false);
            }
        };
        fetchData();
    }, []);

    return { topics, setTopics, data, setData, isloading, setIsloading };
};

export default useFetch;
