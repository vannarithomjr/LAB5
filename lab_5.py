"""
The program is trying to translate a sentence captured as user input.
We first read in the text file textese.txt.
Then from the file, we create a list of strings from each lines in the text file.
Then, we create a dictionary the list.
Once the text file has been read into memory, we close the file.

We then define a function for translating which envolves splitting the user input (sentence) into an
array of strings ("enjoy the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight"]

After each word is translated, we then
print out the translated sentence to the user.
"""


"""
main():
    set sentence = input()
    set dictionary = create_dictionary()
    translate(sentence, dictionary)

translate(sentence, dictionary):
    words = for each of the word, translate the word
    for each words, translate the word
    print translated sentencee to user

create_dictionary():
    read in textese.txt
    create list - each line from file
    close the file
    create a dict off of the list
    return the dict

main()
"""

# This method kickstarts the app
# It creates a dictionary and files off the translate method
def main():
    sentence = input("Enter a sentence: ")
    dictionary = create_dictionary("textese.txt")
    translate(sentence, dictionary)

# This method creates a dictionary based of a text file given a parameter
def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()
    return dict([word.split(",") for word in words])

# This method tranlsates the user input based off of the dictionary
def translate(sentence, dictionary):
    words = sentence.split()
    for word in words:
        print(dictionary.get(word, word), " ", end = " ")

main()