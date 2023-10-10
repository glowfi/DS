import React, { useState } from 'react';
import Tbody from './Tbody';
import Thead from './Thead';

const Search: React.FC<any> = (props) => {
    const [searchterm, setSearchterm] = useState('');
    const { data, topics, getCode } = props.obj;

    const handleChange = (searchterm: any = '') => {
        const out: any = {};

        topics.forEach((topic: any) => {
            const tmp: any = [];
            data[topic].map((prog: any) => {
                if (
                    JSON.stringify(prog)
                        .toLowerCase()
                        .includes(searchterm.toLowerCase())
                ) {
                    tmp.push(prog);
                }
            });
            if (tmp.length > 0) {
                out[topic] = tmp;
            }
        });

        return [out, Object.keys(out)];
    };

    return (
        <div
            className="modal fade"
            id="exampleModal1"
            //@ts-ignore
            tabIndex="-1"
            aria-labelledby="exampleModalLabel1"
            aria-hidden="true"
        >
            <div className="modal-dialog modal-dialog-scrollable modal-lg">
                <div className="modal-content">
                    <div className="modal-header">
                        <h5 className="modal-title" id="exampleModalLabel1">
                            List of Programs Present
                        </h5>
                        <button
                            type="button"
                            className="btn-close"
                            data-bs-dismiss="modal"
                            id="klose1"
                            aria-label="Close"
                            onClick={() => {
                                setSearchterm('');
                            }}
                        ></button>
                    </div>
                    <div className="modal-body" id="modbody1">
                        <div className="form-group my-3">
                            <input
                                type="text"
                                className="form-control"
                                id="search"
                                aria-describedby="Search Programs"
                                placeholder="Start Typing ..."
                                value={searchterm}
                                onChange={(e) => {
                                    setSearchterm(e.target.value);
                                    handleChange(e.target.value);
                                }}
                            />
                        </div>
                        {topics
                            ? // @ts-ignore
                              handleChange(searchterm)[1].map(
                                  (topic: any, idx: any) => {
                                      return (
                                          <div
                                              className="accordion-item my-3"
                                              key={idx}
                                          >
                                              <table className="table table-striped table-dark">
                                                  <Thead />
                                                  <Tbody
                                                      topic={topic}
                                                      data={
                                                          handleChange(
                                                              searchterm
                                                          )[0]
                                                      }
                                                      getCode={getCode}
                                                  />
                                              </table>
                                          </div>
                                      );
                                  }
                              )
                            : ''}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default React.memo(Search);
