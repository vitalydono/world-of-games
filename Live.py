from MemoryGame import play as play_memory_game
from GuessGame import play as play_guess_game
from CurrencyRouletteGame import play as play_currency_roulette_game


def get_choosen_game_number():
    try:
        choosen_number = int(
            input("Choose a game number that you want to play: "))
        if choosen_number not in range(1, 4):
            print("The choosen_game_number is not optionally available")
            return False
        else:
            return choosen_number
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return False


def get_choosen_difficulty_number():
    try:
        choosen_difficulty = int(input("Choose a difficulty level from 1-5: "))
        if choosen_difficulty not in range(1, 6):
            print("The choosen_game_number is not optionally available")
            return False
        else:
            return choosen_difficulty
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return False


def welcome(name):
    return f"Hello {name} and welcome to the World of Games. Here you can find many cool games to play."


def get_endgame_text(name, result):
    text_by_result = {
        0: f"Too bad, {name} \nyou have lost...",
        1: f"Well done, {name} \nyou won the game!"
    }
    return text_by_result[result]


def load_game():
    print("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n2. Guess Game - guess a number and see if you chose like the computer.\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS.")

    choosen_game_number = get_choosen_game_number()
    if not choosen_game_number:
        get_choosen_game_number()
    choosen_game_difficulty = get_choosen_difficulty_number()
    if not choosen_game_difficulty:
        get_choosen_difficulty_number()

    if choosen_game_number == 1:
        memory_game_result = play_memory_game(choosen_game_difficulty)
        return memory_game_result, choosen_game_difficulty
    elif choosen_game_number == 2:
        guess_game_result = play_guess_game(choosen_game_difficulty)
        return guess_game_result, choosen_game_difficulty
    elif choosen_game_number == 3:
        currency_roulette_game_result = play_currency_roulette_game(
            choosen_game_difficulty)
        return currency_roulette_game_result, choosen_game_difficulty
