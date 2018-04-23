# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division
from random import randint
import sys
from decimal import Decimal


def roll(total, count):
    total_to_be_rolled = total * 100
    assert total_to_be_rolled == int(total_to_be_rolled)
    sep_points = set()
    while len(sep_points) != count - 1:
        point = randint(1, total_to_be_rolled)
        if point not in sep_points:
            sep_points.add(point)
    return sep_points

if __name__ == '__main__':
    total, count = sys.argv[1:]
    total = Decimal(total)
    count = int(count)
    result = roll(total, count)
    sorted_points = sorted(Decimal(e)/100 for e in result)
    sorted_points.insert(0, Decimal('0.00'))
    sorted_points.append(total)
    for i in range(1, count + 1):
        print('#{}: {}'.format(i, sorted_points[i] - sorted_points[i - 1]))
