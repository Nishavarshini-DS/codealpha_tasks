import random
import time
import sys

def print_with_delay(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

words = ["python", "apple", "chair", "house", "music"]
answer = random.choice(words)
guesses = []
incorrect_guesses = 0
max_incorrect = 6

print_with_delay("Welcome to Hangman!\n")
print_with_delay("Rules:")
print_with_delay("1) Guess the word")
print_with_delay("2) You have 6 attempts\n")

while incorrect_guesses < max_incorrect:
    display_word = ""
    for letter in answer:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)
    
    if "_" not in display_word:
        print_with_delay("\n🎉 You guessed the word! You win!")
        print_with_delay(f"The word was: {answer}")
        break
        
    guess = input("Guess a letter: ").lower()
    
    if guess in guesses:
        print_with_delay("You already guessed that letter.")
    elif guess in answer:
        print_with_delay("Correct!")
        guesses.append(guess)
    else:
        print_with_delay("Wrong!")
        guesses.append(guess)
        incorrect_guesses += 1

if incorrect_guesses == max_incorrect:
    print_with_delay("\n😢 You ran out of guesses.")
    print_with_delay(f"The word was: {answer}")

input("\nPress Enter to exit...")