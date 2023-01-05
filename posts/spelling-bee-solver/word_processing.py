# process words in wiki-100k.txt to only include 
# words that fall within NYT spelling bee constraints
# so as to minimize the amount of space they take up
# in the webpage

import re

with open('words_alpha.txt', 'r') as f:
    words_alpha = set(line.strip() for line in f.readlines())

with open('wiki-100k.txt', 'r') as f:
    words = set()
    while True:
        try:
            line = f.readline()
            if not line:
                break
            else:
                words.add(line.strip())
        except:
            pass

word_regex = r'^[a-z]{4,20}$'
def word_filter(word):
    return (
        bool(re.match(word_regex, word)) and 
        len(set(word)) <= 7 and
        word in words_alpha
    )

prev_length = len(words)

filtered_words = []
for word in words:
    if word_filter(word):
        filtered_words.append(word)

print('Filtered {} words down to {}'.format(
    prev_length, len(filtered_words)
))

f = open('spelling_bee_words.txt', 'w')
out = '["'
chunksize = len(filtered_words)//100
for line in range(100):
    out += '", "'.join(filtered_words[chunksize * line:chunksize * (line+1)])
    out += '",\n"'
out = out[:-3] + ']'
f.write(out)
f.close()
