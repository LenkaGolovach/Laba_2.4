#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    sum = 0
    count = 0

    for i in range(0, len(A)):
        if A[i] % 2 == 0:
            sum += A[i]
            count += 1

    print("Сумма равна - ", sum, "\nКол-во равно - ", count)