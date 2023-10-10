import React from 'react';

const Thead: React.FC<any> = () => {
    return (
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Problem</th>
                <th scope="col">Difficulty</th>
                <th scope="col">Code</th>
            </tr>
        </thead>
    );
};

export default React.memo(Thead);
