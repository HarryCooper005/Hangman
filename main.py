#import libraries
import random
import json
import time

#initiate variables
guessed = False
lives = 9
LETTERS = []
GUESSED = []
WORD = []
WORDGUESSED = []

#opens the word list
WORDS = json.loads(open("words.json").read())

#picks a random word from the list
word = WORDS[random.randint(0,len(WORDS)-1)]
#sets the word to all lowercase
word = word.lower()

#creates a blank array which is shown during the program
for letter in word:
    GUESSED.append("_")
    WORD.append(letter)
    WORDGUESSED.append(letter)

#creates the loop
while not guessed and lives != 0:

    #clears the shell/console/terminal
    print("\n"*100)

    #prints the amount of lives the player has
    print("Lives:",lives)

    #prints the letters that have been guessed by the player
    print("Guessed Letters:")
    for i in LETTERS:
        print(i, end = " ")

    print()

    #prints the blank and correctly guessed characters
    for i in GUESSED:
        print(i, end = " ")

    print("")

    #testing - remove when complete
    #for i in WORD:
    #    print(i, end = "")

    #print("")

    #guess input
    guess = input("Guess: ")

    if len(guess) == 1 and guess.isalpha():
        #checks if the letter has already been guessed
        if guess.lower() not in LETTERS:

            #if the letter hasn't already been guessed checks if the letter is in the random word or not
            if guess.lower() in WORD:
                #checks if the letter is in the word more than once
                if WORD.count(guess.lower()) > 1:
                    #if the letter is in the word more than once then it will replace the letters in the list with a "_"
                    for i in range(WORD.count(guess.lower())):
                        #adds the letters to the GUESSED array in the correct place
                        GUESSED[WORD.index(guess.lower())] = WORD[WORD.index(guess.lower())]

                        WORD[WORD.index(guess.lower())] = "_"

                    #adds the letter to the LETTERS array to show that it has been guessed
                    LETTERS.append(guess.lower())

                else:
                    #replaces the letter with a "_"
                    GUESSED[WORD.index(guess)] = WORD[WORD.index(guess)]
                    WORD[WORD.index(guess.lower())] = "_"

                    #adds the letter to the LETTERS array to show that it has been guessed
                    LETTERS.append(guess.lower())


            else:
                #adds the letter to te LETTERS array to show that it has been guessed
                LETTERS.append(guess.lower())

                #removes a life
                lives -= 1

        else:
            pass

        #initiates the SAME array
        SAME = []
        #checks if the GUESSED array (letter correctly guessed) is the same as the WORDGUESSED array (target word)
        for i in range(len(GUESSED)):
            if GUESSED[i] != WORDGUESSED[i]:
                #if the selected letter is not the same in the arrays then False will be added to the SAME array
                SAME.append(False)

            else:
                #else, it will just pass
                pass

        #if there is no False's in teh SAME array the guessed will be set to True
        if False not in SAME:
            guessed = True

        else:
            #else it will just pass
            pass

    else:
        print("invalid input")

if guessed == True:
    #if the word is guessed correctly then it will print "You Win!" and the correct word
    print("You Win!")
    print(word)

else:
    #if all the lives are lost then it will print "You lose" and the correct word
    print("You Lose")
    print("The Word Was",word)

#the program will pause for 5 seconds before closing
time.sleep(5)
