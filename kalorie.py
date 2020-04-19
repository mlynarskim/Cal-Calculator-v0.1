# -*- coding: utf-8 -*-
import os
import sys
import math
print("Oblicz dzienne zapotrzebowanie kaloryczne")
name = input("Podaj swoje imię: \n")
if name[-1] == "a":
    name = int(-161)
else:
    name = int(+5)
height = int(input("Podaj swój wzrost w centymetrach: \n"))
weight = int(input("Podaj swoją wagę w kilogramach: \n"))
age = int(input("Podaj swój wiek \n"))
ppm = (10 * weight) + (6.25 * height) - (5 * age) + name
print("Wybierz aktywnosc")
print("Praca siedząca, brak dodatkowej aktywności fizycznej \n [a]")
print("Praca niefizyczna, mało aktywny tryb życia \n [b]")
print(
    "Lekka praca fizyczna, regularne ćwiczenia 3-4 razy print(ok. 5h) w tygodniu \n [c]")
print(
    "Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu \n [d]")
print("Praca fizyczna ciężka, regularne ćwiczenia 7 razy w tygodniu \n [e] ")
activity = input()
if activity == "a":
    activity = 1.2
elif activity == "b":
    activity = 1.4
elif activity == "c":
    activity = 1.6
elif activity == "d":
    activity = 1.8
elif activity == "e":
    activity = 2.0
print("Dzienne zapotrzebowanie kaloryczne wynosi:", ppm * activity, "kcal")
