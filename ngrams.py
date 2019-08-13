import re

def calc_ngram():
    type = None
    while type == None:
        result = raw_input("What type of NGram (unigram | bigram)? ")
        if(result == "unigram" or result == "bigram"):
            type = result

    if(result == "unigram"):
        calc_unigram()

    if(result == "bigram"):
        calc_bigram()

def calc_unigram():
    word = raw_input("Please enter your word: ")

    test = get_corpus_one()
    vocabulary_set = set(test)

    occurrence_count = len(re.findall(word, test))
    word_count = len(re.findall("\\w+", test))

    print("Occurrence rate: {}/{}".format(occurrence_count, word_count))
    print("P(w) = {}".format(float(occurrence_count) / word_count))
    print("PLaplace(wi) = {}").format(float(occurrence_count + 1) / (word_count + len(vocabulary_set)))

def calc_bigram():
    word = raw_input("Please enter your word: ")
    preceding_word = raw_input("Please enter the preceding word: ")

    test = get_corpus_one()
    vocabulary_set = set(test)

    occurrence_count = len(re.findall(preceding_word + " " + word, test))
    word_count = len(re.findall(preceding_word, test))

    print("Occurrence rate: {}/{}".format(occurrence_count, word_count))
    print("P(w(n) | w(n-1)) = {}".format(float(occurrence_count) / word_count))
    print("PLaplace(w(n) | w(n-1)) = {}".format(float(occurrence_count + 1) / (word_count + len(vocabulary_set))))

def get_corpus_one():
    return get_file_contents("alice_in_wonderland_by_lewis_carroll.txt")

def get_corpus_two():
    return get_file_contents("pride_and_prejudice_by_jane_austen.txt")

def get_file_contents(file_name):
    f=open(file_name, "r")
    if f.mode == 'r':
        return f.read()

calc_ngram()