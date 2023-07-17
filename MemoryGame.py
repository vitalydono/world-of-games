import random
import time
import sys
import functools


def generate_sequence(Difficulty):
    sequence_numbers = []
    while len(sequence_numbers) < Difficulty:
        sequence_numbers.append(random.randint(1, 101))
    sys.stdout.write(f"{sequence_numbers}")
    sys.stdout.flush()
    time.sleep(0.7)
    sys.stdout.write("'\r                   ")
    print([])
    return sequence_numbers

# TODO: add protection if the user put value that not a int


def get_list_from_user(Difficulty):
    selected_numbers = []
    while len(selected_numbers) < Difficulty:
        select_number = int(input("Select a number: "))
        selected_numbers.append(select_number)

    return selected_numbers


def is_list_equal(random_sequence, choosen_sequence):
    if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, random_sequence, choosen_sequence), True):
        return True
    else:
        return False


def play(Difficulty):
    random_sequence = generate_sequence(Difficulty)
    num_of_guesses = 0
    while num_of_guesses < 3:
        choosen_sequence = get_list_from_user(Difficulty)
        result = is_list_equal(random_sequence, choosen_sequence)
        if result:
            return result

        print('no...\n')
        num_of_guesses += 1

    return result
