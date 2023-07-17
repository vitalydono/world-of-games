import random

max_value_by_diff = {
    1: 3,
    2: 5,
    3: 7,
    4: 9,
    5: 11,
}


def generate_number(Difficulty):
    return random.randint(1, max_value_by_diff[Difficulty])


def get_guess_from_user(Difficulty):
    try:
        max_value = max_value_by_diff[Difficulty]
        number = int(input(f"Choose a number between 1 and {max_value}: \n"))
        if number not in range(1, max_value):
            print(f"You must to choose a number between 1 and {max_value}\n")
    except ValueError:
        print("Invalid value, must be a number\n")

    return number


def compare_results(secret_number, guessed_user_number):
    return secret_number == guessed_user_number


def play(Difficulty):
    secret_number = generate_number(Difficulty)
    num_of_guesses = 0
    while num_of_guesses < 3:
        guessed_user_number = get_guess_from_user(Difficulty)
        result = compare_results(secret_number, guessed_user_number)

        if result:
            return result
        print('no...\n')
        num_of_guesses += 1

    return result
