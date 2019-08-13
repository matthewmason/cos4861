filename = raw_input("Please enter the file name from which to read:")

f = open("pos_tagged.txt","r")
contents = f.read().split()

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

input_file = open(filename,"r")
input_file_contents = input_file.read().split()

output = []
for word in input_file_contents:
    if word in most_likely_word_types:
        output.append(word + '/' + most_likely_word_types[word])
    else:
        output.append(word + '/NN')

print(output)
output_file = open("output.txt","w+")
output_file.write(" ".join(output))
