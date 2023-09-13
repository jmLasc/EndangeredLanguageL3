def transcribe_lines():
    with open("atayal_stripped6.13.lateruse.txt", "r") as input_file:
        lines = input_file.readlines()

    output_lines = []
    current_line = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        if line.startswith(("'", '"')) or line[0].isalpha():
            current_line += line + " "
        elif current_line:
            output_lines.append(current_line.strip())
            current_line = ""

    if current_line:
        output_lines.append(current_line.strip())

    with open("atayal_stripped6.13.final_output.txt", "w") as output_file:
        for line in output_lines:
            output_file.write(line + "\n")

transcribe_lines()
