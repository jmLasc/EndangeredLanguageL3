# This code removes brackets and the text between
import re
import sys
import os
from pathlib import Path
# bracket chars = ()[]（）- ascii parens, ascii brackets, fullwidth parens

final = [file for file in os.listdir(".") if re.search(".*final.*\.txt", file.lower())]
if len(final) != 1:
    print("""More than one .txt file with "final" in its name.\nPlease rename so that only one of these exists in the current directory.""")
    quit()

text = ''
with open(final[0], encoding='utf8') as file:
    text += file.read()

text = re.sub(r"\(.*?\)|\[.*?\]|\（.*?\）", "", text)
text = re.sub(r"[\(\)\[\]\（\）]", " ", text) # Catch leftovers

pdf_name = os.path.basename(os.getcwd())
filename = pdf_name + "_no_bracket_no_text.txt"
fullpath = os.path.join(os.getcwd(), filename)

if filename not in os.listdir("."):
    Path(fullpath).touch()

with open(filename, 'w', encoding='utf8') as file:
    file.write(text)