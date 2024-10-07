# Utility Functions for the Game
import time, random
from game_riddles import riddle_list, hint_list

def riddle(x):
    print(f"\n{riddle_list[x][0]}\n")

def hint(y):
    print(f"\n{hint_list[y]}\n")

def solve_riddle(z):
    player_answer = input("\nWie lautet die Antwort auf das Rätsel?\n").capitalize()
    correct_answer = riddle_list[z][1]
    if player_answer == correct_answer:
        print("\nKorrekt! Du hast das Rätsel erfolgreich gelöst!")
        # riddle_list.remove[riddle_list[z]]
        # hint_list.remove[z]
        input("In welche Richtung möchtest du nun gehen? Norden, Süden, Westen oder Osten?\n")
        return False
    else:
        print("Das war leider nicht korrekt. Probiere es gerne erneut.")
        return True

def end_game():
    print("\nDu siehst es durch die nächste Tür bereits funkeln und glitzern.")
    print("Du hast es geschafft, du gelangst in die Schatzkammer!")
    print("Credits:\nAuthor: Zerrelius \nThanks to: Dicu and Velriha\n")
    input("Drücke die Enter Taste um den aktuellen Run (Gameplay) zu beenden.\n")
    return False