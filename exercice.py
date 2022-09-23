#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number *= -1
    return number
# More advvanced function: abs()


def use_prefixes() -> list[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    names = []
    for letter in prefixes:
        names.append(letter+suffixe)
    return names


def prime_integer_summation() -> int:
    count = 0
    number = 2
    sum = 0

    while count < 100:

        for i in range(2, number):
            if number % i == 0: # Not prime
                break
        else: # Prime
            count += 1
            sum += number

        number += 1

    return sum

def factorial(number: int) -> int:
    factorial = 1
    for i in range(2, number+1): # Start at 2 and stops at number (included).
        factorial *= i
    return factorial


def use_continue() -> None:
    for i in range(1, 10+1):
        if i == 5:
            continue
        print(i)

def verify_ages(groups: List[List[int]]) -> List[bool]:
    result = ""
    for group in groups:
        if 25 in group:
            result += f"{str(True)} "
            continue
        if len(group) <= 3 or len(group) > 10:
            result += f"{str(False)} "
            continue
        if min(group) < 18:
            result += f"{str(False)} "
            continue
        if max(group) > 70 and 50 in group:
            result += f"{str(False)} "
            continue

        result += f"{str(True)} "

    return result.split()


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
