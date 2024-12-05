#!/bin/python

import glob
import os
import shutil
from gen import languages as lang
from gen import sort_file_folders


base_lang = lang["python"]["name"]
base_dir_base_lang = lang["python"]["location"]
base_lang_ext = lang["python"]["extension"]
base_lang_comment = lang["python"]["comment_string_single_line"]

new_lang = lang["go"]["name"]
base_dir_new_lang = lang["go"]["location"]
new_lang_ext = lang["go"]["extension"]
new_lang_comment = lang["go"]["comment_string_single_line"]
extra_text_after_first_line = lang["go"]["extra_text_after_first_line"]


# Create base directory for new lang
if os.path.exists(base_dir_new_lang):
    shutil.rmtree(base_dir_new_lang)
os.mkdir(base_dir_new_lang)


# Create files corresponding to topics
directories = sort_file_folders(glob.glob(f"./Programs/{base_lang}/*"))

for directory in directories:
    topic = os.path.basename(directory)
    directoryPath = f"{base_dir_new_lang}/{topic}"
    os.mkdir(directoryPath)
    files = sort_file_folders(glob.glob(f"{directory}/*"))
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
