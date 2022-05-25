import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(word)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)   #tracks all the letters of the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    #getting user input
    while len(word_letters)>0 and lives>0:

        #used letters 
        print("You have ",lives ,"lives left and you have used these letters : ", " ".join(used_letters))

        #what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word : ", " ".join(word_list))

        user_letter = input("Guess a letter : ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1 #takes a life 

        elif user_letter in used_letters:
            print("You have already guessed this character. Try again.")
        else:
            print("Invalid character. Try again.")
    if lives == 0:
        print("You died, sorry, the word was", word)
    else:
        print("You guessed the word ",word,"!!")


# user = input("Type something : ")
# print(hangman)
hangman()