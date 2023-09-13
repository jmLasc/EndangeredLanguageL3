def highlight_lines(file1, file2):
    # Read the contents of the files
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Iterate through the lines of file1 and check for matching characters in file2
    highlighted_lines1 = []
    for line1 in lines1:
        line1_chars = set(line1.strip())
        matching_chars_found = False

        for line2 in lines2:
            line2_chars = set(line2.strip())
            if line1_chars.intersection(line2_chars):
                matching_chars_found = True
                break

        if matching_chars_found:
            highlighted_lines1.append('**' + line1)
        else:
            highlighted_lines1.append(line1)

    # Write the highlighted lines back to file1
    with open(file1, 'w', encoding='utf-8') as f1:
        f1.writelines(highlighted_lines1)


# Provide the file paths to compare
file1_path = 'atayal_stripped.txt'
file2_path = 'atayal_stripped2.txt'

highlight_lines(file1_path, file2_path)
