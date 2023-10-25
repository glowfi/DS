import React from 'react';

const Tbody: React.FC<any> = ({ topic, data, getCode }) => {
    return (
        <tbody id={`${topic}`}>
            {data
                ? //@ts-ignore
                  data[topic].map(
                      ([
                          number,
                          _,
                          __,
                          problemStatement,
                          problemLink,
                          difficulty,
                          code
                      ]: String[]) => {
                          return (
                              <tr key={Date.now + Math.random().toFixed(5)}>
                                  <th scope="row">{number}</th>
                                  <td>
                                      <a
                                          href={`${problemLink}`}
                                          target="_blank"
                                      >
                                          {problemStatement}
                                      </a>
                                  </td>
                                  <td>
                                      {difficulty.trim() === 'Easy' ? (
                                          <span className="badge bg-success">
                                              {difficulty}
                                          </span>
                                      ) : difficulty.trim() === 'Medium' ? (
                                          <span className="badge bg-warning">
                                              {difficulty}
                                          </span>
                                      ) : difficulty.trim() === 'Hard' ? (
                                          <span className="badge bg-danger">
                                              {difficulty}
                                          </span>
                                      ) : (
                                          'unknown'
                                      )}
                                  </td>
                                  <td>
                                      <button
                                          type="button"
                                          className="btn btn-success"
                                          data-bs-toggle="modal"
                                          data-bs-target="#exampleModal"
                                          id={`${number}-${topic}-${code}`}
                                          onClick={() => {
                                              const url = code;
                                              getCode(url);
                                          }}
                                      >
                                          Code
                                      </button>
                                  </td>
                              </tr>
                          );
                      }
                  )
                : ''}
        </tbody>
    );
};

export default React.memo(Tbody);
