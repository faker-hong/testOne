import random

word_file = "words.txt"
word_list = []

with open(word_file, 'r') as words:
    for word in words:
        word = word.strip().lower()
        if 3 < len(word) < 8:
            word_list.append(word)


def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)


print(generate_password())