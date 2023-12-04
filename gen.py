#!/bin/python

import glob
import os
import json
import pandas as pd

# Create Sheet
os.remove("./sheet.csv")
f = open("sheet.csv", "a", encoding="utf-8")
f.write(f"#,Type,Problem,Link,Difficulty,Code\n")
f.close()


PROGRAM_LOCATION = "https://raw.githubusercontent.com/glowfi/DS/main/Programs"
directories = sorted(glob.glob("./Programs/*"))
dic = {}
idx = 0

for directory in directories:
    print(f"Parsing {directory} ....")
    if os.path.isdir(f"./{directory}"):
        files = glob.glob(f"{directory}/*")
        currentData = []
        for file in files:
            with open(f"{file}") as f:
                first_line = f.readline()
                data = first_line.split(",")

                try:
                    if data[1]:
                        dataStructureType = file.split("/")[2].split("_")[1]
                        link = data[0].strip(" ").replace("# ", "")
                        difficulty = data[1].strip("\n")

                        tmp = file.split("/")[-1].strip(" ").replace(".py", "")
                        extractNumber = tmp.split("_")[0]
                        problemStatement = " ".join(tmp.split("_")[1:])

                        loc = "/".join(file.split("/")[2:])
                        code = f"{PROGRAM_LOCATION}/{loc}"

                        currentData.append(
                            [
                                int(extractNumber),
                                dataStructureType,
                                problemStatement,
                                link,
                                difficulty,
                                code,
                            ]
                        )
                except Exception as e:
                    name = file.split("./")[-1]
                    print(f"Exception Handled for {name}!")

        currentData.sort(key=lambda x: x[0])

        # Save dict to work with JSON
        dataStructureType = currentData[0][1]
        dic[dataStructureType] = currentData

        # Create CSV
        for (
            extractNumber,
            dataStructureType,
            problemStatement,
            link,
            difficulty,
            code,
        ) in currentData:
            f = open("sheet.csv", "a", encoding="utf-8")
            f.write(
                f"{idx},{dataStructureType},{problemStatement},{link},{difficulty},{code}\n"
            )
            idx += 1
            f.close()

# Dump JSON
json_object = json.dumps(dic, indent=4)
with open("data.json", "w") as outfile:
    outfile.write(json_object)

# Dump Readme
df = pd.read_csv("sheet.csv")
markdown_table = df.to_markdown()
title = "A collection of data-structures and algorithms"
img = "\n![LOGO](./logo.jpg)\n"
with open("README.md", "w") as rf:
    rf.write(f"# DS\n\n> {title}\n{img}\n{markdown_table}")
