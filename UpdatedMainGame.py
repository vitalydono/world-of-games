from Live import load_game, welcome, get_endgame_text
from Score import add_score


person_name = input("Enter your name: ")

print(welcome(person_name))

result, difficulty = load_game()
add_score(difficulty, result)

print(get_endgame_text(person_name, result))
