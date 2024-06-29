import Link from 'next/link';

const NotFound = () => {
    return (
        <div className="text-center flex flex-col justify-center items-center h-dvh">
            <h1 className="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl border-b-4">
                404
            </h1>

            <p className="mt-4">
                <Link
                    href="/"
                    className="hover:opacity-75 transition-all text-blue-500"
                >
                    Go to home
                </Link>
            </p>
        </div>
    );
};

export default NotFound;
