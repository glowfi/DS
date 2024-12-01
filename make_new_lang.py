#!/bin/python

import glob
import os
import re


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]
    return sorted(data, key=alphanum_key)


base_lang = "python"
base_dir_base_lang = os.path.abspath(f"./Programs/{base_lang}")
base_lang_ext = "py"

new_lang = "go"
base_dir_new_lang = os.path.abspath(f"./Programs/{new_lang}")
new_lang_ext = "go"


# Create base directory for new lang
os.mkdir(base_dir_new_lang)


directories = sorted_alphanumeric(glob.glob(f"./Programs/{base_lang}/*"))

for directory in directories:
    topic_directory = f"{base_dir_new_lang}/{directory.split("/")[-1]}"
    os.mkdir(topic_directory)
    if os.path.isdir(f"./{directory}"):
        files = glob.glob(f"{directory}/*")
        currentData = []
        for file in files:
            file_ext_allowed = file.find("py")
            if file_ext_allowed != -1:
                name = os.path.basename(file)
                with open(f"{directory}/{name}", "r") as fp:

                    if name.split(".")[-1] == base_lang_ext:
                        data = fp.readlines()
                        with open(
                            f"{topic_directory}/{name.split('.')[0]}.{new_lang_ext}",
                            "w",
                        ) as fp:
                            fp.write(data[0])
                    else:
                        data = fp.read()
                        with open(
                            f"{topic_directory}/{name.split('.')[0]}.{name.split('.')[-1]}",
                            "w",
                        ) as fp:
                            fp.write(data)
