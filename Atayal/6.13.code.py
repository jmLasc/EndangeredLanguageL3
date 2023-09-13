def add_return_bar_before_regex(regex_pattern, input_file, output_file):
    import re

    # Read the content from the input file
    with open(input_file, 'r') as file:
        text = file.read()

    # Add the return bar before the occurrences of the regex pattern
    updated_text = re.sub(regex_pattern, r'\n\g<0>', text)

    # Write the updated text to the output file
    with open(output_file, 'w') as file:
        file.write(updated_text)

# Specify the input and output file paths
input_file = 'atayal_stripped6.12.lateruse.txt'
output_file = 'atayal_stripped6.13.lateruse.txt'

# Specify the regex pattern to add return bars before
pattern = r' 2'

# Call the function to perform the task
add_return_bar_before_regex(pattern, input_file, output_file)
