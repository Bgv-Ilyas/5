#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    n = int(input("Введите натуральное число n: "))
    r = n % 7
    k = n // 7
    if r == 0:
        print(f"n = 7*{k}")
    else:
        print(f"n = 7*{k} + {r}")