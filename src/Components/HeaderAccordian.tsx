import React from 'react';

const HeaderAccordian: React.FC<any> = ({ numberToWords, idx, topic }) => {
    return (
        <h2
            className="accordion-header"
            id={`flush-heading${numberToWords(idx + 1)}`}
        >
            <button
                className="accordion-button"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target={`#flush-collapse${numberToWords(idx + 1)}`}
                aria-expanded="false"
                aria-controls={`flush-collapse${numberToWords(idx + 1)}`}
            >
                {topic}
            </button>
        </h2>
    );
};

export default React.memo(HeaderAccordian);
