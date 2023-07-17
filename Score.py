from Utils import SCORES_FILE_NAME


def POINTS_OF_WINNING(difficulty): return (difficulty * 3) + 5


def add_score(difficulty, result):
    try:
        if result:
            with open(SCORES_FILE_NAME, "r+") as file:
                current_score = int(file.read())
                new_score = current_score + POINTS_OF_WINNING(difficulty)
                file.seek(0)
                file.write(str(new_score))
    except FileNotFoundError:
        with open(SCORES_FILE_NAME, "w") as file:
            new_score = POINTS_OF_WINNING(difficulty)
            file.write(str(new_score))
