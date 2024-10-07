# Utility Functions for the Game
import time, random

riddle_list = [
    ["Ich bin nicht am Leben, aber ich wachse. Ich habe keine Lungen, aber ich brauche Luft. Was bin ich?", "Feuer"],
    ["Zwei Väter und zwei Söhne gingen angeln. Jeder von ihnen fing einen Fisch, aber am Ende waren nur drei Fische im Korb. Wie ist das möglich?", "Ein Großvater, ein Sohn und ein Enkel"],
    ["Du bist mein Sohn, aber ich bin nicht dein Vater. Wer hat das gesagt?", "Mutter"]
]

hint_list = [
    "Du siehst auf einer Wand einen brennenden Wald auf einem Gemälde.",
    "Auf einem Gemälde an einer Wand erblickst du eine Familie, bestehend aus Männern. Einen Grauhaarigen Mann links, einen großen Braunhaarigen rechts und ihnen beiden steht ein Kind.",
    "Du erblickst eine Statue einer Frau wie sie ein Bündel eines Babys im Arm hält."
]

def riddle():
    global riddle_number
    riddle_number = (int(random.randint(0,len(riddle_list))))-1
    print(f"\n{riddle_list[riddle_number][0]}\n")

def hint():
    print(f"\n{hint_list[riddle_number]}\n")

def solve_riddle():
    answer = input("Wie lautet die Antwort auf das Rätsel?")

def end_game():
    print("Das Game endet hier")