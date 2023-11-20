#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    a = float(input("Введите действительное число a: "))
    b = float(input("Введите действительное число b: "))
    c = float(input("Введите действительное число c: "))

    numbers = [a, b, c]
    numbers.sort()
    print(f"Числа в порядке возрастания: {numbers[0]}, {numbers[1]}, {numbers[2]}")
    numbers.reverse()
    print(f"Числа в порядке убывания: {numbers[0]}, {numbers[1]}, {numbers[2]}")