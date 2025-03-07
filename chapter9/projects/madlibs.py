#! python3
# madlibs.py - Reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
# Usage: python madlibs.py <filename>
# Example: python madlibs.py madlibs.txt

import sys, re

if len(sys.argv) < 2:
    print('Usage: python madlibs.py <filename>')
    with open('madlibs.txt', 'w') as filename:
        filename.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
    print('madlibs.txt created with default content.')
    # sys.exit()

# elif not sys.argv[1].endswith('.txt'):
#     print('Please provide a text file.')
#     sys.exit()
elif len(sys.argv) > 2:
    print('Please provide only one text file.')
    sys.exit()

filename = sys.argv[1] if len(sys.argv) == 2 else 'madlibs.txt'

# Read the file
with open(filename, 'r') as file:
    content = file.read()

# Find the words to replace
words = re.findall(r'(ADJECTIVE|NOUN|ADVERB|VERB)', content)

# Replace the words

for word in words:
    new_word = input(f'Enter an {word.lower()}: ')
    content = re.sub(word, new_word, content, 1)

# Write the new content to a new file

new_filename = f'{filename[:-4]}_new.txt'
with open(new_filename, 'w') as new_file:
    new_file.write(content)

print(f'New file created: {new_filename}')
print(content)