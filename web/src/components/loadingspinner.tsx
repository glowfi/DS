import { Loader2 } from 'lucide-react';
import React from 'react';

interface LoadingSpinnerProps {
    name?: string;
}

const LoadingSpinner: React.FunctionComponent<LoadingSpinnerProps> = ({
    name
}) => {
    return (
        <div className="flex justify-center items-center min-h-fit">
            <div className="flex gap-3 items-center justify-center">
                <Loader2 className="my-4 h-8 w-8 animate-spin" />
                <p>Loading {name}...</p>
            </div>
        </div>
    );
};

export default LoadingSpinner;
