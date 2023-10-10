import React from 'react';

const Navbar: React.FC<any> = ({ total }) => {
    const handleSource = () => {
        window.open('https://github.com/glowfi/DS', '_blank');
    };
    const showAuthor = () => {
        window.open('https://github.com/glowfi/', '_blank');
    };

    return (
        <nav className="navbar navbar-expand-lg navbar-dark">
            <div className="container-fluid">
                <a
                    className="navbar-brand fw-bold"
                    href="https://glowfi.github.io/DS/"
                >
                    SDE Sheet
                </a>
                <button
                    className="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent"
                    aria-controls="navbarSupportedContent"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div
                    className="collapse navbar-collapse"
                    id="navbarSupportedContent"
                >
                    <ul className="navbar-nav mx-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                            <button
                                type="button"
                                className="btn btn-danger mx-2 my-2"
                                id="nprog"
                            >
                                Total Code(s) = {total}
                            </button>
                        </li>
                        <li className="nav-item">
                            <button
                                type="button"
                                className="btn btn-light mx-2 my-2"
                                id="sourcecode"
                                onClick={handleSource}
                            >
                                Source Code
                            </button>
                        </li>
                        <li className="nav-item">
                            <button
                                type="button"
                                className="btn btn-success mx-2 my-2"
                                data-bs-toggle="modal"
                                data-bs-target="#exampleModal1"
                                id="search"
                            >
                                Search
                            </button>
                        </li>
                    </ul>

                    <button
                        className="btn btn-dark btn-outline-dark fw-bold"
                        id="person"
                        onClick={showAuthor}
                    >
                        glowfi
                    </button>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;
