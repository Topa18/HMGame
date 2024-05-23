import random
import json
from pathlib import Path


words = ['absurd', 'abyss', 'avenue', 'awkward' 'banjo', 'bikini', 'blizzard', 
    'cobweb', 'crypt', 'cycle', 'duplex', 'dwarves', 'equip', 'fly', 
    'onyx', 'puzzle', 'queue', 'quiz', 'rhythm', ' rock', 'staff', 
    'strong', 'telephone', 'unknown', 'vampire', 'gossip', 'hell', 'ice',
    'jackpot', 'jazz', 'juice', 'kayak', 'kiwi', 'luck', 'leg', 
    'luxary', 'matrix', 'night', 'wave', 'wizard', 'yummy', 'zombie']

menu = """Welcome to HangManGame!\n
    1 - Play game
    2 - Player statistics
    3 - Delete player
    4 - Exit\n"""

scores_dir = 'HangMan/scores.json'

if not Path(scores_dir).exists():
    with open(scores_dir, 'w') as scores:
        scores.write('{}')

def create_player_stat(player_name):
    with open(scores_dir) as scores:
        scores_dict = json.loads(scores.read())
        players = scores_dict.keys()
        if not player_name in players:
            scores_dict[player_name] = {"total_games": 0, "wins": 0, "losses": 0}
            scores_json = json.dumps(scores_dict, indent=3)    
            scores.close()
            with open(scores_dir, "w") as scores:
                scores.write(scores_json)
    return print(f"Nice to meet you, {player_name}, let`s play!\n")

def delete_player_stat(player_name):
    with open(scores_dir) as scores:
        scores_dict = json.loads(scores.read())
        players = scores_dict.keys()
        if player_name in players:
            del scores_dict[player_name]
            scores_json = json.dumps(scores_dict, indent=3)
            scores.close()
            with open(scores_dir, "w") as scores:
                scores.write(scores_json)
            return print(f"Player \"{player_name}\" was successfully deleted\n")
        elif not player_name in players:
            return print("No such player")

def update_wins_stat(player_name):
    with open(scores_dir) as scores:
        scores_dict = json.loads(scores.read())
        scores_dict[player_name]["total_games"] += 1
        scores_dict[player_name]["wins"] += 1
        scores_json = json.dumps(scores_dict, indent=3)
        scores.close()
        with open(scores_dir, "w") as scores:
            scores.write(scores_json)
    return print(f"\nCongrats, {player_name}! You won!")

def update_losses_stat(player_name):
    with open(scores_dir) as scores:
        scores_dict = json.loads(scores.read())
        scores_dict[player_name]["total_games"] += 1
        scores_dict[player_name]["losses"] +=1
        scores_json = json.dumps(scores_dict, indent=3)
        scores.close()
        with open(scores_dir, "w") as scores:
            scores.write(scores_json)
    return print(f"\nYou lose, {player_name} :(")

def show_player_stat():
    with open(scores_dir) as scores:
        scores_dict = json.loads(scores.read())
        for stat in scores_dict.items():
            print(stat,'\n')
        return print("Back to menu\n")

def ask_to_play_again():
    again = input(str("Want to play again?\nYes or no: "))
    if again == "Yes" or again =="yes":
       return start_hm_game(player_name)
    elif again == "No" or again == "no":
       return print("Thank you for playing!\n\n"), print(menu)

def start_hm_game(player_name):
    lives = 10
    answer = random.choice(words)
    hidden_word = list(answer)
    word = ['-' for char in hidden_word]
    used_letters = []
    
    while True:
        if lives == 0:
            update_losses_stat(player_name)
            return print(f"\nIt was - \'{answer}\'\n"), ask_to_play_again()
        if word == list(answer):
            update_wins_stat(player_name)
            return ask_to_play_again()
            
        print("answer is - ", answer)
        print(f"You have {lives} lives left")
        print(f"Guess: {word}\n")

        turn = str(input("Enter the letter: "))
        if turn in used_letters:
            print(f"You alredy has used letter {turn}")
            continue
        if turn not in hidden_word:
            print('False!')
            lives -= 1
        else:
            print('True!')
            for let, try_ in zip(hidden_word, word):
                if turn == let:
                    word[hidden_word.index(let)] = turn
                    hidden_word[hidden_word.index(let)] = try_
        
        used_letters.append(turn)


print(menu)
while True:
    command = int(input("Print number to choose option: "))
    if command == 1:
        player_name = str(input("Enter your name: "))
        create_player_stat(player_name)
        start_hm_game(player_name)
    elif command == 2:
        show_player_stat()
        print(menu)
        continue
    elif command == 3:
        with open(scores_dir) as scores:
            print("\nPlayers in scores: ")
            scores_dict = json.loads(scores.read())
            for player in scores_dict.keys():
                print('-' + player)
        player_name = str(input("\nWhich player statistics you want to delete?: "))
        delete_player_stat(player_name)
        print(menu)
        continue
    elif command == 4:
        print("Bye!")
        break
    else:
        print("No such command, try again")
        continue