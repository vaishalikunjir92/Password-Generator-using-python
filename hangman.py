import random

from numpy.lib.function_base import place

word_list = ["aardvark","baboon","camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it

chosen_word = random.choice(word_list)
game_over = False
print(chosen_word)

# TODO - Create placeholder with same number of blanks as the chosen_word
placeholder = ""
for position in range(len(chosen_word)):
    placeholder +="_"
print(placeholder)

#TODO-2 - Ask the user to guess a leetter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter ").lower()
#print(guess)

#TODO-3 - Check if the user guessed(guess) is one of the letters in the chosen_word. Print "Right" if it is , "Wrong" if its not.
display=""
for letter in chosen_word:
    if letter == guess:
       # print("Right")
        display += letter
    else:
        display+="_"
        # print("Wrong")
print(display)

if "_" not in display:
    game_over = True
    print("You win.")
