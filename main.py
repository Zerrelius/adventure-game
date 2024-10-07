# Main Part of: Die verlorene Schatzsuche
import time, random
from game_utils import riddle, hint, solve_riddle, end_game
from game_rooms import room_name, room_description
from game_riddles import riddle_list, hint_list

def greeting():
    print("Herzlich Willkommen im Text Adventure: Die verloren Schatzsuche!")
    print("_____\n")
    print("Die Spielregeln sind einfach. Du musst durch verschiedene Kammern in einem Dungeon gehen.")
    print("Jede Kammer verlangt das du ein Rätsel lösen musst um weiter zu kommen.")
    print("Anschließend erhältst du die Wahl in Richtung 'Norden', 'Süden', 'Osten' als auch 'Westen' weiter zu gehen.")
    print("Du kommst erst weiter wenn das Rätsel gelöst ist. Achte auf die Räume, sehe sie dir genau an und ache vielleicht auf Gegenstände die du mitnehmen kannst.")

def enter_room():
    global room_number
    room_number = (int(random.randint(0,len(room_name))))-1
    print(f"Du betrittst {room_name[room_number]}. Wenn du dich umsiehst, erblickst du")
    description(room_number)

def description(room_description_number):
    for element in room_description[room_description_number]:
        print(f"{element}")
    print("-----")

def main():
    gameplay = True
    new_riddle = True
    solved = 0
    difficulty = 3

    while True:
        print("Herzlich Willkommen im Text Adventure: Die verloren Schatzsuche!")
        print("-----\n")
        print("1. Das Spiel starten")
        print("2. Die Regeln einmal durch lesen (Kommen auch zum Spielstart)")
        print("3. Schwierigskeitsgrad einstellen")
        print("4. Das Spiel beenden.")
        print("-----\n")

        choose = input("Was möchtest du tun?\n")

        if choose == "1":
            greeting()
            print("Das Spiel beginnt!\n-----\n")
            gameplay = True

            while gameplay == True:
                enter_room()
                riddle_number = (int(random.randint(0,len(riddle_list))))-1
                new_riddle = True

                while new_riddle == True:
                    print("1. Dir das Rätsel ansehen")
                    print("2. Nach Hinweisen suchen")
                    print("3. Das Rätsel lösen")
                    print("4. Zurück ins Hauptmenü. ACHTUNG: Dein Fortschritt wird NICHT gespeichert.")
                    print("-----")
                    do_choose = input("Was möchtest du tun?\n")

                    if do_choose == "1":
                        riddle(riddle_number)

                    elif do_choose == "2":
                        hint(riddle_number)

                    elif do_choose == "3":
                        new_riddle = solve_riddle(riddle_number)
                        if new_riddle == False:
                            solved = solved + 1
                            if solved == difficulty:
                                gameplay = end_game()
                                print("Du hast das Game erfolgreich beendet!")
                                print("-----\n")

                    elif do_choose == "4":
                        print("Das Spiel wird unterbrochen und du kommst zurück ins Hauptmenü.")
                        gameplay = False
                        break
                    else:
                        print("Bitte wähle zwischen 1, 2, 3 oder 4.")

        elif choose == "2":
            greeting()

        elif choose == "3":
            print("\nWelchen Schwiergikeitsgrad möchtest du wählen?")
            print("1. Einfach (3 Rätsel)")
            print("2. Mittel (6 Rätsel)")
            print("3. Schwer (9 Rätsel)")
            print("-----")
            choose_difficulty = input("Welchen Schwierigkeitsgrad möchten sie? Einfach ist die Standard Einstellung\n")
            if choose_difficulty == "1":
                difficulty = 3
                print("Sie haben den einfachen Schwierigkeitsgrad gewählt.\n")
            elif choose_difficulty == "2":
                difficulty = 6
                print("Sie haben den mittelschweren Schwierigkeitsgrad gewählt.\n")
            elif choose_difficulty == "3":
                difficulty = 9
                print("Sie haben den schwierigen Schwierigkeitsgrad gewählt.\n")
            else:
                print("Bitte wählen Sie nur zwischen 1, 2 oder 3")

        elif choose == "4":
            print("Das Spiel wird beendet. Auf Wiedersehen!")
            break

        else:
            print("Bitte wähle zwischen 1, 2, 3 oder 4.")

main()