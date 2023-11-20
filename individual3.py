#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    goose_legs = 2
    rabbit_legs = 4
    total_legs = 64

    combinations = []
    for g in range(0, total_legs // goose_legs + 1):
        r = (total_legs - g * goose_legs) // rabbit_legs
        if r >= 0 and (total_legs - g * goose_legs) % rabbit_legs == 0:
            combinations.append((g, r))
    print(f"Возможные сочетания гусей и кроликов: {combinations}")
