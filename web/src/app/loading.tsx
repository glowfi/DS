import LoadingSpinner from '../components/loadingspinners/loadingspinner';

const loading = () => {
    return (
        <div className="flex justify-center items-center h-dvh">
            <LoadingSpinner name="page" />
        </div>
    );
};

export default loading;
