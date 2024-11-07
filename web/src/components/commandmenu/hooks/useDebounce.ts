import { useEffect, useState } from 'react';

export const useDebounce = (value: string, delay = 300) => {
    const [debouncedText, setDebouncedText] = useState('');
    const [isloadingtxt, setIsloadingtxt] = useState(true);

    useEffect(() => {
        const timeout = setTimeout(() => {
            setDebouncedText(value);
            setIsloadingtxt(false);
        }, delay);

        return () => clearTimeout(timeout);
    }, [value, delay]);

    return [debouncedText, isloadingtxt, setIsloadingtxt];
};
