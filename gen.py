#!/bin/python

import glob
import os
import json
import re
import pandas as pd

# Create Sheet
if os.path.exists("./sheet.csv"):
    os.remove("./sheet.csv")
f = open("sheet.csv", "a", encoding="utf-8")
f.write(f"#,Type,Problem,Link,Difficulty,Code,Language\n")
f.close()


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]
    return sorted(data, key=alphanum_key)


langs = ["python", "go"]
allowed_exts = ["py", "go"]
dic = {}

for index, language in enumerate(langs):
    PROGRAM_LOCATION = (
        f"https://raw.githubusercontent.com/glowfi/DS/main/Programs/{language}"
    )
    directories = sorted_alphanumeric(glob.glob(f"./Programs/{language}/*"))
    print(directories)
    idx = 0

    for directory in directories:
        print(f"Parsing {directory} ...")
        if os.path.isdir(f"./{directory}"):
            files = glob.glob(f"{directory}/*")
            currentData = []
            for file in files:
                file_ext_allowed = file.find(allowed_exts[index])
                if file_ext_allowed != -1:
                    with open(f"{file}") as f:
                        first_line = f.readline()
                        data = first_line.split(",")

                        try:
                            if data[1]:
                                dataStructureType = (
                                    os.path.dirname(file).split("/")[-1].split("_")[-1]
                                )
                                link = data[0].strip(" ").replace("# ", "")
                                difficulty = data[1].strip("\n").lstrip(" ").rstrip(" ")

                                tmp = file.split("/")[-1].strip(" ").replace(".py", "")
                                extractNumber = tmp.split("_")[0]
                                problemStatement = " ".join(tmp.split("_")[1:]).replace(
                                    f".{allowed_exts[index]}", ""
                                )

                                loc = "/".join(file.split("/")[3:])
                                code = f"{PROGRAM_LOCATION}/{loc}"

                                currentData.append(
                                    [
                                        int(extractNumber),
                                        dataStructureType,
                                        problemStatement,
                                        link,
                                        difficulty,
                                        code,
                                        language,
                                    ]
                                )
                        except Exception as e:
                            name = file.split("./")[-1]
                            print(f"Exception Handled for {name}!", e)

            # Save dict to work with JSON
            currentData.sort(key=lambda x: x[0])
            dataStructureType = currentData[0][1]
            if dataStructureType not in dic:
                dic[dataStructureType] = currentData
            else:
                dic[dataStructureType] = [*dic[dataStructureType], *currentData]

            # Create CSV
            for (
                extractNumber,
                dataStructureType,
                problemStatement,
                link,
                difficulty,
                code,
                lang,
            ) in currentData:
                f = open("sheet.csv", "a", encoding="utf-8")
                f.write(
                    f"{idx},{dataStructureType},{problemStatement},{link},{difficulty},{code},{lang}\n"
                )
                idx += 1
                f.close()

# Dump Custom JSON
final_list = []
for topic in dic:
    idx = 0
    for k in dic[topic]:
        dic[topic][idx] = {
            "id": dic[topic][idx][0],
            "topic": dic[topic][idx][1],
            "problem_name": dic[topic][idx][2],
            "problem_link": dic[topic][idx][3],
            "difficulty": dic[topic][idx][4],
            "solution_link": dic[topic][idx][5],
            "language": dic[topic][idx][6],
        }
        final_list.append(dic[topic][idx])
        idx += 1
json_object = json.dumps(final_list, indent=4)
with open("data.json", "w") as outfile:
    outfile.write(json_object)

# Dump Readme
df = pd.read_csv("sheet.csv")
markdown_table = df.to_markdown(index=False)
title = "A collection of data-structures and algorithms"
img = "\n![LOGO](./logo.jpg)\n"
siteLink = "\n### Hosted Site : https://dssheet.vercel.app"
subHeading = "\n### Questions\n"
with open("README.md", "w") as rf:
    rf.write(f"# DS\n\n> {title}\n{img}{siteLink}\n{subHeading}\n{markdown_table}")
