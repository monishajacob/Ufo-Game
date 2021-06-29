import time
from random import choice
from os import system, name
from ufo import x as images


def random_word():
    """Open nouns.txt file for processing and return a random word."""
    with open('static/nouns.txt', 'r') as read_nouns:
        random_word = choice(read_nouns.readlines()).strip()
    return [random_word.upper(), len(random_word)]


def write_statistics(status, guessed, incorrect_guess):
    """generate statistic file and update it with win/lost status,
       total guessed letters and the correctly guessed letters for each game"""
    total_guessed = len(guessed)
    correct_guess = list(filter(lambda x: x not in incorrect_guess, guessed))
    formatted_correct_guess = "".join(correct_guess)
    with open('static/statistics.txt','a') as statistic_file:
        statistic_file.write(f"{status} {total_guessed} {formatted_correct_guess}\n")


def handle_image(index):
    """Accept index as the parameter and return the image at the index."""
    return images[index]


def print_menu(ind, length):
    """Print the start menu of the game."""
    print('\nUFO: The Game')
    print('Instructions: save us from alien abduction by guessing letters in the codeword.\n')
    print(handle_image(ind))
    print(f'Incorrect Guesses:\n{None}')
    codeword = " ".join(['_']*length)
    print(f'\nCodeword:\n{codeword}')


def get_input(guessed):
    """Check for the validity of the user guessed letter and return it."""
    user_input = input("\nPlease enter your guess: ")
    while len(user_input) > 1 or not user_input.isalpha():
        print('\nI cannot understand your input. Please guess a single letter.\n')
        user_input = input('\nPlease enter your guess: ')
    while user_input in guessed:
        print('\nYou can only guess that letter once, please try again.')
        user_input = input("\nPlease enter your guess: ")
    guessed.add(user_input)
    return user_input.upper()


def check_input(user_guessed, chosen_word):
    """Check if the user guessed letter exist in the randomly chosen word."""
    if user_guessed in chosen_word:
        return True
    else:
        return False


def display_codeword(current_remaining, word, length, letter=""):
    """Accept user guessed letter and return the codeword."""
    for ind in range(length):
        if letter == word[ind]:
            current_remaining[ind] = letter
    return " ".join(current_remaining)


def handle_success(current_remaining, user_guessed, incorrect_guess,
                   word, length):
    """Display the contents when the user guessed a right letter."""
    print("\nCorrect! You're closer to cracking the codeword.\n")
    print(handle_image(len(incorrect_guess)))
    print("\nIncorrect Guesses:")
    print(" ".join(incorrect_guess))
    print(f'\nCodeword:\n{display_codeword(current_remaining, word,length, user_guessed)}')


def handle_failure(current_remaining, user_guessed, incorrect_guess, word,
                   length):
    """Display the contents when the user guessed a wrong letter."""
    print("\nIncorrect! The tractor beam pulls the person in further.\n")
    print(handle_image(len(incorrect_guess)))
    print("\nIncorrect Guesses:")
    print(" ".join(incorrect_guess))
    print(f'\nCodeword:\n{display_codeword(current_remaining, word,length, user_guessed)}')
    # Delighter
    with open('static/messages.txt', 'r') as encourangements:
        encouragement = choice(encourangements.readlines()).strip()
    print(f"\n{encouragement}")


def run_game():
    """Run the game logic."""
    chosen_word, length = random_word()
    remaining_letters = len(set(chosen_word))
    guessed = set()
    incorrect_guess = []
    current_remaining = ['_']*length
    print_menu(len(incorrect_guess), length)

    while len(incorrect_guess) < len(images)-1:
        user_guessed = get_input(guessed)
        correct_guess = check_input(user_guessed, chosen_word)

        if correct_guess:
            remaining_letters -= 1
            if remaining_letters < 1:
                print("\nCorrect! You saved the person and earned a medal of honor!")
                print(f"The codeword is: {chosen_word}.")
                write_statistics("Won", guessed, incorrect_guess)
                break
            else:
                handle_success(current_remaining, user_guessed,
                               incorrect_guess, chosen_word, length)
        else:
            incorrect_guess.append(user_guessed)
            if len(incorrect_guess) == 6:
                print(handle_image(len(incorrect_guess)))
                print("\nSorry you are out of guesses. Better luck next time!")
                print(f"\nThe codeword is: {chosen_word}.")
                write_statistics("Lost", guessed, incorrect_guess)
            else:
                handle_failure(current_remaining, user_guessed,
                               incorrect_guess, chosen_word, length)

    replay = input("\nWould you like to play again (Y/N)? ")
    if replay.upper() == 'Y':
        run_game()
    else:
        print('\nGoodbye!')
        time.sleep(1)
        clear()


def clear():
    """Clear the screen."""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == "__main__":
    run_game()
