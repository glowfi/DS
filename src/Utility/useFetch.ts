import { useEffect, useState } from 'react';
import axios from 'axios';

export const useFetch = (URL: any) => {
    const [response, setResponse] = useState({
        isloading: true,
        iserror: false,
        data: null,
        topics: null,
        totalCodes: 0
    });

    useEffect(() => {
        const getData = async () => {
            try {
                const data = await axios.get(URL);

                let total = 0;
                for (const key in data.data) {
                    total += data.data[key].length;
                }
                setResponse({
                    isloading: false,
                    iserror: false,
                    data: data.data,
                    topics: Object.keys(data.data) as any,
                    totalCodes: total
                });
            } catch (err) {
                console.log(err);
                setResponse({
                    isloading: false,
                    iserror: true,
                    data: null,
                    topics: null,
                    totalCodes: 0
                });
            }
        };

        getData();
    }, []);

    return response;
};
