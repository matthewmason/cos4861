f= open("pos_tagged.txt","r")

contents =f.read().split()

words = {}
most_likely_word_types = {}

for word in contents:
    word_type_pair = word.split('/')
    word_value = word_type_pair[0]
    word_type = word_type_pair[1]

    if word_value not in words:
        words[word_value] = {}

    if word_type in words[word_value]:
        words[word_value][word_type] = words[word_value][word_type] + 1
    else:
        words[word_value][word_type] = 1

for word in words:
    max_count = 0
    type = ''

    for type in words[word]:
        if words[word][type] > max_count:
            type = type
    most_likely_word_types[word] = type

print(most_likely_word_types)
