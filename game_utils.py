# Utility Functions for the Game
import time, random
from game_riddles import riddle_list

points = 0

def riddle(x):
    print(f"\n{riddle_list[x][0]}\n")

def hint(y):
    print(f"\n{riddle_list[y][2]}\n")

def solve_riddle(z):
    player_answer = input("\nWie lautet die Antwort auf das Rätsel?\n")
    correct_answer = riddle_list[z][1]
    if player_answer == correct_answer:
        print("\nKorrekt! Du hast das Rätsel erfolgreich gelöst!")
        riddle_list.remove(riddle_list[z])
        # hint_list.remove[z]
        input("In welche Richtung möchtest du nun gehen? Norden, Süden, Westen oder Osten?\n")
        show_points(3)
        return False
    else:
        print("Das war leider nicht korrekt. Probiere es gerne erneut.")
        show_points(4)
        return True

def end_game():
    print("\nDu siehst es durch die nächste Tür bereits funkeln und glitzern.")
    print("Du hast es geschafft, du gelangst in die Schatzkammer!")
    show_points(1)
    show_points(2)
    print("Credits:\nAuthor: Zerrelius \nThanks to: Dicu and Velriha\n")
    input("Drücke die Enter Taste um den aktuellen Run (Gameplay) zu beenden.\n")
    return False

def show_points(x):
    global points
    if x == 1:
        print(f"Deine Punkte bei diesem Durchlauf: {points}\n")
    elif x == 2:
        points = 0
    elif x == 3:
        points += 10
    elif x == 4:
        points -= 10