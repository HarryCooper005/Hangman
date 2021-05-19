# Hangman in python

This code can be ran in the python IDLE (or other programs that support python code), it uses python 3.8.

# How to use

- Simply open up the main.py file and a random word will be picked from a list of 58,109 english words.
- You will then be given the length of the word in the form fo underscores ("_")
- You will then be prompted to guess a letter
  - it will only accept 1 letter, no numbers/special characters, no blank inputs and no multiple letter inputs
- When you have guessed a letter it will be put into the "guessed letters" bit
  - if the letter guessed is in the word then it will replace the respective underscore in the word
- when you have either guessed the word or ran out of lives, you will be met with the final word and a 5 second delay afterwhich the program will close.
