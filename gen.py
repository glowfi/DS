#!/bin/python

import glob
import os
import json

# Create Sheet
os.remove("./sheet.csv")
f = open("sheet.csv", "a", encoding="utf-8")
f.write(f"Type,Problem,Link,Difficulty,Code\n")
f.write(f",,,,\n")
f.close()


directories = glob.glob("./*")

for directory in directories:
    if os.path.isdir(f"./{directory}"):
        files = glob.glob(f"./{directory}/*")
        currentData = []
        for file in files:
            with open(f"{file}") as f:
                first_line = f.readline()
                data = first_line.split(",")

                dataStructureType = file.split("/")[2].split("_")[1]
                link = data[0].strip(" ").replace("# ", "")
                difficulty = data[1].strip("\n")

                tmp = file.split("/")[-1].strip(" ").replace(".py", "")
                extractNumber = tmp.split("_")[0]
                problemStatement = " ".join(tmp.split("_")[1:])

                loc = "/".join(file.split("/")[2:])
                code = f"https://raw.githubusercontent.com/glowfi/DS/main/{loc}"

                # print(
                #     extractNumber,
                #     dataStructureType,
                #     problemStatement,
                #     link,
                #     difficulty,
                #     code
                # )

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

        currentData.sort(key=lambda x: x[0])

        # Dump JSON
        dataStructureType = currentData[0][1]
        dic = {dataStructureType: currentData}
        json_object = json.dumps(dic, indent=4)

        # Writing to sample.json
        with open("data.json", "w") as outfile:
            outfile.write(json_object)

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
                f"{dataStructureType},{problemStatement},{link},{difficulty},{code}\n"
            )
            f.close()
