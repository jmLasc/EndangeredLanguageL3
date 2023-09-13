# def main():
#     with open('yami_stripped(1.0).txt', 'r') as file1:
#         lines_file1 = file1.readlines()

#     with open('yami_stripped_final.txt', 'r') as file2:
#         lines_file2 = file2.readlines()

#     lines_file1 = [line.strip() for line in lines_file1]
#     lines_file2 = [line.strip() for line in lines_file2]

#     missing_portions = []
#     for line_file1 in lines_file1:
#         found = False
#         for line_file2 in lines_file2:
#             if line_file1 in line_file2:
#                 found = True
#                 break
#         if not found:
#             missing_portions.append(line_file1)

#     for portion in missing_portions:
#         print(portion)

# if __name__ == "__main__":
#     main()


import difflib

def main():
    with open('yami_stripped(1.0).txt', 'r') as file1:
        lines_file1 = file1.readlines()

    with open('yami_stripped_final.txt', 'r') as file2:
        lines_file2 = file2.readlines()

    diff = difflib.unified_diff(lines_file1, lines_file2, lineterm='')
    
    missing_lines = []
    for line in diff:
        if line.startswith('-'):
            missing_lines.append(line[1:])

    for portion in missing_lines:
        print(portion)

if __name__ == "__main__":
    main()
