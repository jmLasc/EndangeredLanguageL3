# This code does the following
# For each folder, process the "..._final.txt" file and make 2 versions
# 1 - Remove all brackets
# 2 - Remove all brackets and the text inside of the brackets

import re
import sys
import os
from pathlib import Path

folders = [folder for folder in os.listdir(os.getcwd()) if os.path.isdir(folder) and not folder[0] == "."]

print("Processing...")

for i, folder in enumerate(folders):
    # Get final scraped file
    final = [file for file in os.listdir(folder)]
    final = [file for file in final if re.search(r".*final.*\.txt", file.lower())]
    if len(final) == 0:
        print("""fail: more than 1 file with the name in the form "...final.txt"\nplease check filenames in folder {0}""".format(folder))

    filepath = os.path.join(os.getcwd(), folder, final[0])
    text = ''
    with open(filepath, encoding='utf8') as f:
        text += f.read()
    
    no_br = re.sub(r"[\(\)\[\]\（\）]", " ", text)

    no_br_no_te = re.sub(r"\(.*?\)|\[.*?\]|\（.*?\）", "", text)
    no_br_no_te = re.sub(r"[\(\)\[\]\（\）]", " ", no_br_no_te) # Catch leftovers

    processed = [no_br, no_br_no_te]

    fname = [folder + "_no_br.txt", folder + "_no_br_no_te.txt"]

    for i, name in enumerate(fname):
        fullpath = os.path.join(os.getcwd(), folder, name)
        if name not in os.listdir(os.path.join(os.getcwd(), folder)):
            Path(fullpath).touch()

        with open(fullpath, 'w', encoding='utf8') as file:
            file.write(processed[i])

print("Done!")