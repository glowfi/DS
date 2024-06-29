import LoadingSpinner from '@/components/loadingspinners/loadingspinner';

const loading = () => {
    return (
        <div className="flex h-dvh">
            <LoadingSpinner name="page" />
        </div>
    );
};

export default loading;
