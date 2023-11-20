#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
if __name__ == '__main__':

    def f(x):
        sum = 0
        n = 0
        e = 10**(-10)
        term = x**n / math.factorial(n)
        while term >= e:
            sum += term
            n += 1
            term = x**n / math.factorial(n)
        return sum

    x = float(input("Введите x: "))

    y = f(x)
    print("Значение функции f(", x, ") =", y)