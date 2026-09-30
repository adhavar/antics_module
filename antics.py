# CIS-117 Lab2
# Write a description of your module here
# Group #2
# Group members:
# Adhamaryz Vargas Atoche
# Kezlyn Margareth
# Christian Strus

def tautogram():
    """
    Check if a text in which all words start with the same letter
    Author: Kezlyn Margareth
    """
    sentence = input('Enter your sentence: ').split()
        
    letter = sentence[0][0]

    if all (word[0] == letter for word in sentence):
        print("Every words in the sentence starts with the same letter!")
    else:
        print("The words in the sentence don't start with the same letter.")

def isogram():
    """
    Check and returns true if a word has no letter of the alphabet occurs more than once
    Author: Kezlyn Margareth
    """
    word = input('Enter your word: ')

    if len(set(word)) == len(list(word)):
        print("The word has no repreated letter!")
    else:
        print("The word has repeated letters")
        

if __name__== "__main__":
    tautogram()
    isogram()