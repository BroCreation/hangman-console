from random import choice
from time import sleep
from hangman_drawing import hangman as wrong_guess_results

words = {'editors': ["sublime", "vim", "emacs", "vscode", "notepad", "codeblocks", "eclipse", "DevCpp"],
        'fruits': ["mango", "apple", "grape", "banana", "pineapple"],
        'subjects': ["maths", "physics", "english", "chemistry", "islamiat"]}

# use sorted for sets and dicts when needed to get a specific 'index' value
word_name, word_list = choice(sorted(words.items()))
word = choice(word_list)
word_hashes = ['_'] * len(word)

def display_game(count):
    print("*" * len(word) * 2)
    for line in wrong_guess_results[count]:
        print(line)
    print(" ".join(word_hashes))
    print("*" * len(word) * 2)

def display_hint():
    sleep(1)
    for name, list in words.items():
        print(f"{name.upper()}: ", end="")
        print(list)

def main():
    wrong_guess_count, attempts = 0, 0
    display_game(wrong_guess_count)
    while True:
        if wrong_guess_count == len(wrong_guess_results) - 2:
            print('-> Secret msg -> \'hint\' -> to view all')
            inp = input("Maybe Enter: ")
            if inp == 'hint':
                display_hint()
                display_game()
                
        guess = str(input(f"Guess the {word_name[0:-1]} name or Get hanged: ").lower())

        if len(guess) > 1 or not guess.isalpha():
            print("Invalid Guess")
            display_game(wrong_guess_count)
            continue

        if guess in word_hashes:
            print("Already Set")
            display_game(wrong_guess_count)
            continue

        attempts += 1

        for i in range(len(word)):
            if guess == word[i]:
                word_hashes[i] = guess

        if guess not in word_hashes:
            wrong_guess_count += 1

        display_game(wrong_guess_count)

        if wrong_guess_count >= (len(wrong_guess_results) - 1):
            print(f"You got yourself hanged dummy! Know your {word_name}.")
            break

        if word_hashes == list(word):
            print(f"You guessed the {word_name[0:-1]} correctly, good job!")
            print(f"Attempts = {attempts}")
            break

def introduction():
    print(f'Welcome to \'Learn the {word_name} with Hangman.\'')
    sleep(1)
    print('Let\'s Begin!')
    sleep(1.5)

if __name__ == "__main__":
    introduction()
    main()
    input('Press Enter to exit: ')