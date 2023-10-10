import React, { useState } from 'react';
import { DATA_URL } from './Utility/constants';
import { useFetch } from './Utility/useFetch';
import numberToWords from './Utility/numberToWords';
import CodeModal from './Components/CodeModal';
import Tbody from './Components/Tbody';
import Thead from './Components/Thead';
import HeaderAccordian from './Components/HeaderAccordian';
import Navbar from './Components/Navbar';
import Search from './Components/Search';

const App: React.FC<{}> = () => {
    const { isloading, iserror, data, topics, totalCodes } = useFetch(DATA_URL);
    const [code, setCode] = useState('...');

    const getCode = async (url: any) => {
        const response = await fetch(url);
        const data = await response.text();
        setCode(data);
    };

    if (isloading && !data) {
        return (
            <>
                <h3>Loading ...</h3>
            </>
        );
    } else if (iserror) {
        return (
            <>
                <h3>Error ...</h3>
            </>
        );
    }

    return (
        <>
            <Search obj={{ data, topics, getCode }} />
            <Navbar total={totalCodes} />
            <div className="container">
                <CodeModal code={code} />

                <div
                    className="accordion accordion-flush"
                    id="accordionFlushExample"
                >
                    {topics
                        ? // @ts-ignore
                          topics.map((topic: any, idx: any) => {
                              return (
                                  <div
                                      className="accordion-item my-3"
                                      key={idx}
                                  >
                                      <HeaderAccordian
                                          numberToWords={numberToWords}
                                          idx={idx}
                                          topic={topic}
                                      />
                                      <div
                                          id={`flush-collapse${numberToWords(
                                              idx + 1
                                          )}`}
                                          className="accordion-collapse collapse"
                                          aria-labelledby={`flush-heading${numberToWords(
                                              idx + 1
                                          )}`}
                                          data-bs-parent="#accordionFlushExample"
                                      >
                                          <div className="accordion-body">
                                              <table className="table table-striped table-dark">
                                                  <Thead />
                                                  <Tbody
                                                      topic={topic}
                                                      data={data}
                                                      getCode={getCode}
                                                  />
                                              </table>
                                          </div>
                                      </div>
                                  </div>
                              );
                          })
                        : ''}
                </div>
            </div>
        </>
    );
};

export default App;
