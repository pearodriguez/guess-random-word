import random 
import string
from word_list import words

def main(): 
    keep_playing = 'y'

    while keep_playing == 'y':
       play_word_guess()
       keep_playing = input('Would you like to play again? (y/n) ')



def play_word_guess(): 
    display_options()
    word_length = int(input())

    word_choice = num_letter_choice(words, word_length)
    word_letters = set(word_choice)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # setting number of attempts
    if len(word_choice) == 3:
        attempts = 6
    elif len(word_choice) == 4:
        attempts = 6
    elif len(word_choice) == 5:
        attempts = 10

    # getting user letter
    while len(word_letters) > 0 and attempts > 0:
        # display letters already used 
        print('\nYou have', attempts, 'attempts left')
        print('You have used these letters:', ' '.join(used_letters))

        # display current word 
        word_list = [letter if letter in used_letters else '-' for letter in word_choice]
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else: 
                attempts -= 1 
                print('Letter is not in word')
        elif user_letter in used_letters:
            print('Letter already guessed')
        else: 
            print('Not a valid character')
    if attempts == 0:
        print('\nYou lost')
        print('This was your word: ', word_choice)
    else: 
        print('\nCongrats! Here is your word:', word_choice)


# chooses random word from list
def get_word(words): 
    random_word = random.choice(words)
    return random_word.upper()

# gets word based on length (3 - 5 letter words)
def get_three_letter_word(words): 
    random_word = random.choice(words)
    while len(random_word) != 3: 
        random_word = random.choice(words)
    return random_word.upper()

def get_four_letter_word(words): 
    random_word = random.choice(words)
    while len(random_word) != 4: 
        random_word = random.choice(words)
    return random_word.upper()

def get_five_letter_word(words): 
    random_word = random.choice(words)
    while len(random_word) != 5: 
        random_word = random.choice(words)
    return random_word.upper()

# one fuction choose letter length (3 - 5 letter)
# return uppercase w/ random_word.upper()
def num_letter_choice(words, num): 
    if num == 1: 
        random_word = random.choice(words)
        while len(random_word) != 3: 
            random_word = random.choice(words)
        return random_word.upper()
    elif num == 2: 
        random_word = random.choice(words)
        while len(random_word) != 4: 
            random_word = random.choice(words)
        return random_word.upper()
    elif num == 3: 
        random_word = random.choice(words)
        while len(random_word) != 5: 
            random_word = random.choice(words)
        return random_word.upper()
# def guess_word(): 

# prints guessing options
def display_options(): 
    print('\nWelcome to Guess the Word' + '\nChoose length of word ' + \
    '\n1) three letter word' + '\n2) four letter word' + '\n3) five letter word' )


main()