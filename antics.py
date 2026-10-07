# CIS-117 Lab2
# The module contains 6 functions to 
# Group #2
# Group members:
# Adhamaryz Vargas Atoche
# Kezlyn Margareth
# Christian Strus

def palindrome(sentence):
    """
    Check if a word or sentence that reads the same backwards
    Author: Kezlyn Margareth
    """
    if sentence == sentence[::-1]:
        return True
    else:
        return False


def pangram(phrase):
    '''
    The function checks if a phrase or sentence contains all 26 letters of the alphabet.
    Author: Adhamaryz Vargas
    '''

    alphabet = "abcdefghklmnopqrstuvwxyz"

    for letter in alphabet:
        if letter.lower() in phrase:
            continue
        else:
            return False 
    return True

def tautogram(sentence):
    """
    Check if a text in which all words start with the same letter
    Author: Kezlyn Margareth
    """
    words = sentence.split()  
    letter = words[0][0]

    if all (word[0] == letter for word in sentence):
        return True
    else:
      return False

def isogram(word):
    """
    Check and returns true if a word has no letter of the alphabet occurs more than once
    Author: Kezlyn Margareth
    """

    if len(set(word)) == len(word):
       return True
    else:
       return False


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