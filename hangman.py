#
#
# Hangman game
# Author: Ganesh Zilpe
#

# -----------------------------------
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter in lettersGuessed:
            continue
        else:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            result = result + letter
        else:
            result = result +'_'
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in array:
        if letter in lettersGuessed:
            continue
        result = result+ letter
    return result


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    print "Welcome to the game, Hangman!"
    print 'I am thinking of a word that is '+str(len(secretWord))+' letters long.'
    chances = 8
    alreadyGuessed = ''
    while chances > 0:
        print "-------------";
        print "You have "+str(chances)+" guesses left."
        print "Available letters: "+getAvailableLetters(lettersGuessed)
        alreadyGuessed = getAvailableLetters(lettersGuessed)
        inputchar = raw_input('Please guess a letter: ')
        inputchar = str(inputchar)
        inputchar = inputchar.lower()
        lettersGuessed.append(str(inputchar))
        if inputchar not in alreadyGuessed:
            print "Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed)
            continue
        if inputchar not in secretWord:
            print "Oops! That letter is not in my word: "+getGuessedWord(secretWord, lettersGuessed)
            chances = chances - 1
            continue
        if isWordGuessed(secretWord, lettersGuessed):
            print "Good guess: "+getGuessedWord(secretWord, lettersGuessed)
            print "------------"
            print "Congratulations, you won!"
            break
        else:
            print "Good guess: "+getGuessedWord(secretWord, lettersGuessed)
    print "------------"
    print "Sorry, you ran out of guesses. The word was else."








# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
