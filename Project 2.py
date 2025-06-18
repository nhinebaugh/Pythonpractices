# Nathan Hinebaugh
# CSC2017
# Project 1

# read the text file attached
# converts all words to lowercase,
# prints out all words that begins with letter a, the letter b, and so on.
# Build a dictionary whose keys are the lowercase letters,
# and whose values are sets of words which begin, with that key letter
# After processing the data,
# print the dictionary to the screen in alphabetical order aligned in two fixed sized columns.

# def function
def read_file():
    # def variables
    words = open("/Users/nathanhinebaugh/PycharmProjects/CSC 1017 practice/Project 2/words2.txt", "r")
    word_list = words.readlines()

    words_dict = {}
    # makes all words lower case, strips all whitespace
    for current_word in word_list:
        key = current_word[0].lower()

        value = current_word.lower().rstrip()  # a,b,c

        words_dict[key] = value

        if value in words_dict:
            words_dict[value] = key
    # closes doc and returns
    words.close()
    return words_dict


# def new function

def print_dict():
    # variables
    words_dict = read_file()
    keys = sorted(words_dict.keys())
    # sorts dictionary
    for key in keys:
        words = sorted(words_dict.values())
        print(f"{key} : {words}")

    return words_dict


def main():
    read_file()
    print_dict()


if __name__ == "__main__":
    main()
