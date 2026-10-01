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


def abedecerian(word):
    '''
    The fuction checks if a word's letters appear in alphabetical order or not.
    Author: Adhamaryz Vargas
    '''

    # Initializes a new variable, assigning word to avoid modifying the user's input
    update_word = word

    # while loop
    while len(update_word) > 1:
        # The first character's ASCII of update_word is assigned to a 
        a = ord(update_word[0])

        # The second character's ASCII of update_word is assigned to b
        b = ord(update_word[1])

        # a and b are compared
        if a <= b:
            # update_word is updated without the first character of updated_word
            update_word = update_word[1:]
        else:
            return False
    return True

def dobloon(word):
    '''
    The function checks if every letter in a word appears exactly twice.
    Author: Adhamaryz Vargas
    '''

    # for loop: Iteration of each letter in the word
    for letter in word:
        # Counts the number of times a letter appears in the word
        count = word.count(letter)
        if count == 2:
            # If the count of the letter tested is exactly 2, the loop continues
            continue
        else:
            return False
    return True