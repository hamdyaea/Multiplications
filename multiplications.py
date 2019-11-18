#!/usr/bin/python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

import random
from easygui import *
import sys


def start():
    count = 1
    bonne_rep = 0
    max = 20

    while count <= max:
        number_a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        number_b = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        random.shuffle(number_a)
        random.shuffle(number_b)
        print(str(count) + str(")"))
        print(str(number_a[0]) + str(" X ") + str(number_b[0]) + str(" ="))
        answer = int(input())
        good_ans = int((number_a[0]) * (number_b[0]))
        if good_ans == answer:
            print("Bonne réponse ! Bravo !")
            count = count + 1
            bonne_rep = bonne_rep + 1
        else:
            print("Mauvaise réponse !")
            print(("La réponse était :") + str(good_ans))
            count = count + 1
            bonne_rep = bonne_rep - 1
            if bonne_rep <= 0:
                bonne_rep = 0
        if count > max:
            break
    total = ((bonne_rep) * 6) / 20
    if total == 0:
        total = 1
        image = "./Pictures/sad.jpg"
        msg = "Tu n'as pas réussi\n\nNote finale : " + str(total)
        choices = ["Replay", "Quit"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Replay":
            start()
        else:
            sys.exit(0)
        reply = buttonbox(msg, image=image, choices=choices)
    elif total <= 3:
        total = total + 1
        image = "./Pictures/sad.jpg"
        msg = "Tu n'as pas réussi\n\nNote finale : " + str(total)
        choices = ["Replay", "Quit"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Replay":
            start()
        else:
            sys.exit(0)
    elif total == 6:
        image = "./Pictures/happy.jpeg"
        msg = "Tu as réussi\n\nNote finale : " + str(total)
        choices = ["Replay", "Quit"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Replay":
            start()
        else:
            sys.exit(0)
    elif total > 4 and total < 6:
        total = total + 1
        if total > 6:
            total = 6
        image = "./Pictures/happy.jpeg"
        msg = "Tu as réussi\n\nNote finale : " + str(total)
        choices = ["Replay", "Quit"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Replay":
            start()
        else:
            sys.exit(0)


start()
