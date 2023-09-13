import re

# def split_sentences(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as file:
#         content = file.read()

#     # Splitting sentences based on Chinese punctuation
#     split_content = []
#     lines = content.splitlines()
#     for line in lines:
#         sentences = []
#         sentence = ''
#         for char in line:
#             sentence += char
#             if char in ['！', '。', '？']:
#                 # Check if the sentence starts with romanized characters
#                 if sentence[0].isalpha():
#                     sentences.append(sentence.strip())
#                     sentence = ''
#         if sentence:
#             sentences.append(sentence.strip())

#         # Adding a newline if there are multiple sentences in the line
#         if len(sentences) > 1:
#             split_content.append('\n'.join(sentences))
#         else:
#             split_content.extend(sentences)

#     # Writing the split sentences to the output file
#     with open(output_file, 'w', encoding='utf-8') as file:
#         file.write('\n'.join(split_content))

def extract_sentences(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove content within parentheses and brackets
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\[[^\]]*\]', '', text)

    # Identify sentences based on the specified criteria
    sentences = re.findall(r'[a-zA-Z\'\"].*?[！。？]', text, re.DOTALL)

    # Write the extracted sentences to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for sentence in sentences:
            file.write(sentence + '\n')


# Usage Example
extract_sentences('yami_stripped_final.txt', 'yami_stripped_nospace.txt')


