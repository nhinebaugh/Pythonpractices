# Nathan Hinebaugh
# CSC2017
# Project 1

# psudocode
# open file in read mode, read the file into a list of individual words
# create a main() with 2 other
# sort the list of words in alphabetical order
# write code to read and count each word and put the words and each count into a file.

# defines a function
def format_list():
    # def needed variables
    word_list = open("words.txt", "r")
    words_on_doc = []
    amount_of_words = []

    # reads the list
    words = word_list.readlines()
    # makes all words lower and strips new lines
    for words in words:
        words = words.lower()
        words = words.rstrip()
        # appends words_on_doc list to add new words
        if words not in words_on_doc:
            words_on_doc.append(words)
        # appends amount_of_words list
        amount_of_words.append(words)
    #sorts and returns words_on_doc
    words_on_doc.sort()
    return words_on_doc

#def new function
def output_to_file():
    #declares variable opens new file and creates word_count and next_word lists
    sorted_count = open("words.count.txt", "w")
    words_on_doc = format_list()
    word_count = 0
    next_word = 0

    #determines if words are not the same to write only new words and counts them
    for words in words_on_doc:
        if words != next_word:
            if next_word is not words:
                sorted_count.write(f"{next_word}:{word_count}\n")
            next_word = words
            word_count += 1
        else:
            word_count += 1
    #closes the file
    sorted_count.close()
    #prints a confimation statement
    print(f'Count information stored in "words.count".')

#defines the main and calls other functions
def main():
    format_list()
    output_to_file()
    print(f"Word count complete please see file.")

if __name__ == "__main__":
    main()
