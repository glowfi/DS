#!/bin/python

import json
import re
import glob
import os
from typing import TypedDict
from parse import Approach, parse_file


# Question type
class Question(TypedDict):
    id: int
    topic: str
    problem_name: str
    problem_link: str
    difficulty: str
    solution_link: str
    language: str
    approaches: dict[str, Approach]


# Language type
class Language(TypedDict):
    name: str
    comment_string_single_line: str
    extension: str
    location: str
    extra_text_after_first_line: str


def getProblemName(filename: str) -> str:
    idx = -1
    for i, char in enumerate(filename):
        if char == "_":
            idx = i
            break

    if idx != -1:
        return filename[idx + 1 :].replace("_", " ")
    return ""


def sort_file_folders(data: list[str]) -> list[str]:
    """
    Sorts a list of directory names alphabetically, considering numeric prefixes.

    Args:
        data (list[str]): A list of directory names.

    Returns:
        list[str]: The sorted list of directory names.
    """

    def convert(text):
        """Converts a character to its integer value if it's a digit, otherwise converts it to lowercase."""
        return int(text) if text.isdigit() else text.lower()

    def alphanum_key(key):
        """Creates a tuple of tuples where each inner tuple contains a string and its corresponding integer value."""
        return [convert(c) for c in re.split("([0-9]+)", key)]

    # Use the custom sorting key to sort the directories
    return sorted(data, key=alphanum_key)


def extensionExists(languages: dict[str, Language], extension: str):
    for language in languages:
        if languages[language]["extension"] == extension:
            return True
    return False


def buildSolutionLink(language: str, file: str):
    base_git_url = "https://raw.githubusercontent.com/glowfi/DS/main/Programs"
    return f"{base_git_url}/{language}/{file}"


languages: dict[str, Language] = {
    "python": {
        "name": "python",
        "comment_string_single_line": "#",
        "extension": ".py",
        "location": os.path.abspath("./Programs/python"),
        "extra_text_after_first_line": "",
    },
    "go": {
        "name": "go",
        "comment_string_single_line": "//",
        "extension": ".go",
        "location": os.path.abspath("./Programs/go"),
        "extra_text_after_first_line": "\npackage main",
    },
}

final_data: list[Question] = []


for language in languages.keys():
    base_lang: str = languages[language]["name"]
    base_dir_new_lang: str = os.path.abspath(f"./Programs/{base_lang}")
    directories: list[str] = sort_file_folders(glob.glob(f"{base_dir_new_lang}/*"))
    for directory in directories:
        topic: str = os.path.basename(directory)
        directoryPath: str = f"{base_dir_new_lang}/{topic}"
        files: list[str] = sort_file_folders(glob.glob(f"{directory}/*"))
        questionCount: int = 1
        for file in files:
            name, extension = os.path.splitext(file)
            filename = os.path.basename(name)
            if extensionExists(languages, extension):
                with open(f"{file}") as fp:
                    first_line = fp.readline()
                    data = (
                        first_line.replace(
                            languages[language]["comment_string_single_line"], ""
                        )
                        .strip(" ")
                        .strip("\n")
                    ).split(",")
                    if len(data) < 2:
                        print(f"Skipping {file}")
                        continue
                    else:
                        problem_link, difficulty = data
                        approach = parse_file(file)
                        newQuestion: Question = {
                            "id": questionCount,
                            "topic": topic.split("_")[1],
                            "language": languages[language]["name"],
                            "difficulty": difficulty.strip(" "),
                            "problem_name": getProblemName(filename),
                            "problem_link": problem_link,
                            "solution_link": buildSolutionLink(
                                languages[language]["name"],
                                f"{topic}/{filename}{languages[language]["extension"]}",
                            ),
                        }
                        final_data.append(newQuestion)
                        questionCount += 1

with open("data.json", "w") as data:
    data.write(json.dumps(final_data, indent=4))
