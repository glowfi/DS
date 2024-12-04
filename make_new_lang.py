#!/bin/python

import glob
import os
import re
import shutil
from gen import languages as lang


base_lang = lang[0]["name"]
base_dir_base_lang = lang[0]["location"]
base_lang_ext = lang[0]["extension"]
base_lang_comment = lang[0]["comment_string_single_line"]

new_lang = lang[1]["name"]
base_dir_new_lang = lang[1]["location"]
new_lang_ext = lang[1]["extension"]
new_lang_comment = lang[1]["comment_string_single_line"]
extra_text_after_first_line = lang[1]["extra_text_after_first_line"]


def sort_directories(data: list[str]) -> list[str]:
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


# Create base directory for new lang
if os.path.exists(base_dir_new_lang):
    shutil.rmtree(base_dir_new_lang)
os.mkdir(base_dir_new_lang)


# Create files corresponding to topics
directories = sort_directories(glob.glob(f"./Programs/{base_lang}/*"))

for directory in directories:
    topic = os.path.basename(directory)
    directoryPath = f"{base_dir_new_lang}/{topic}"
    os.mkdir(directoryPath)
    files = glob.glob(f"{directory}/*")
    for file in files:
        name, extension = os.path.splitext(file)
        filename = os.path.basename(name)

        with open(file, "r") as fp:
            if extension == base_lang_ext:
                data = fp.readlines()
                with open(f"{directoryPath}/{filename}{new_lang_ext}", "w") as fp:
                    if (
                        base_lang_comment
                        and new_lang_comment
                        and extra_text_after_first_line
                    ):
                        fp.write(
                            data[0].replace(base_lang_comment, new_lang_comment)
                            + extra_text_after_first_line
                        )
            else:
                data = fp.read()
                with open(
                    f"{directoryPath}/{filename}{extension}",
                    "w",
                ) as fp:
                    fp.write(data)
