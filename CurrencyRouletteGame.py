import random


def get_currency_rate():
    return 3.5


def get_money_interval(difficulty, random_number):
    current_rate = get_currency_rate()
    lower_bound = random_number - (5 - difficulty)
    upper_bound = random_number + (5 - difficulty)
    return lower_bound * current_rate, upper_bound * current_rate


def get_guess_from_user():
    return float(input("Enter your guess for the value in ILS: "))


def compare(lower_bound, upper_bound, user_guess):
    if lower_bound <= user_guess <= upper_bound:
        return True
    else:
        return False


def play(Difficulty):
    random_number = random.randint(1, 100)
    num_of_guesses = 0
    while num_of_guesses < 3:

        lower_bound, upper_bound = get_money_interval(
            Difficulty, random_number)
        print(f"Guess the value of {random_number} USD in ILS.")
        user_guess = get_guess_from_user()
        result = compare(lower_bound, upper_bound, user_guess)
        if result:
            return result
        print('no...\n')
        num_of_guesses += 1

    return result
