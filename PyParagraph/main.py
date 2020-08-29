# import and path the txt file
import os
import re
path = os.path.join("resources", "paragraph.txt")

# reading txt file
with open(path, encoding='utf-8') as text:
    paragraph = text.read()
    
    # get rid of empty lines and split by period
    paragraph = paragraph.replace("\n", " ")
    lines = paragraph.split(".")

    # get rid of every blanks in the lines list
    for n in range(lines.count("")):
        lines.remove("")

    # split the paragraph into words by separating special keys and spaces
    words = re.split("[-,.?! ]", paragraph)

    # get rid of every blanks in the words list
    for n in range(words.count("")):
        words.remove("")

# count the number of characters in each letter into a separate list
char_amount = []
for x in range(len(words)):
    char_amount.append(len(words[x]))

# calculate averages
av_letters = round(sum(char_amount) / len(words), 1)
av_words = round(len(words) / len(lines), 1)

# printing final result
print(f'Paragraph Analysis')
print(f'-----------------')
print(f'Approximate Word Count: {len(words)}')
print(f'Approximate Sentence Count: {len(lines)}')
print(f'Average Letter Count: {av_letters}')
print(f'Average Sentence Length: {av_words}')

# export as text
outpath = os.path.join("analysis", "analysis_result.txt")
with open(outpath, "w") as text:
    text.write(f'Paragraph Analysis \n')
    text.write(f'----------------- \n')
    text.write(f'Approximate Word Count: {len(words)} \n')
    text.write(f'Approximate Sentence Count: {len(lines)} \n')
    text.write(f'Average Letter Count: {av_letters} \n')
    text.write(f'Average Sentence Length: {av_words} \n')