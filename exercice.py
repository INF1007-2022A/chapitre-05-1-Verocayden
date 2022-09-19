#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number *= -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    names = []
    for letter in prefixes:
        names.append(letter+suffixe)
    return names


def prime_integer_summation() -> int:
    count = 1
    prime_count = 0
    summation = 0
    while prime_count <= 100:
        is_prime = True
        for i in range(2, count-1):
            if (count % i) == 0:
                is_prime = False
        if is_prime == True:
            summation += count
            prime_count += 1
        count += 1
    summation -= 1

    return summation

def factorial(number: int) -> int:
    count = 1
    factorial = 1
    while count < number:
        factorial *= count
        count += 1
    return factorial


def use_continue() -> None:
    count = 1
    while count <= 10:
        if count == 5:
            count += 1
            continue
        elif count !=5:
            print(count)
            count += 1


def verify_ages(groups: List[List[int]]) -> List[bool]:
    group_list = []
    for group in groups:
        if 25 in group:
            group_list.append('True')
        elif len(group) <= 3 or len(group) > 10:
            group_list.append('False')
        else:
            for age in group:
                if age < 18:
                    group_list.append("False")
                    break
                elif age > 70:
                    if age == 50:
                        group_list.append("False")
                        break
            else:
                group_list.append('True')

    return group_list


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
