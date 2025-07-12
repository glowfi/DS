import Link from 'next/link';

const NotFound = () => {
    return (
        <div className="flex flex-col justify-center items-center h-screen text-white">
            <h1 className="text-6xl font-extrabold tracking-tight mb-4">404</h1>
            <p className="text-lg mb-6 text-gray-400">
                Sorry, we couldn't find the page you're looking for.
            </p>
            <Link
                href="/"
                className="bg-blue-600 hover:bg-blue-500 text-white font-semibold py-3 px-6 rounded-lg shadow-md transition-all transform hover:scale-105"
            >
                Go to Home
            </Link>
        </div>
    );
};

export default NotFound;
