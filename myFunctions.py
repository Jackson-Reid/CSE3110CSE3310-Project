"""
title: common functions for the unit
author: Jackson Reid
date-created: 2021-02-03
"""

import random, statistics, time


def getAverage(LIST):
    return statistics.mean(LIST)


def getTime():
    return time.perf_counter()


def getSimpleList():
    return [1, 5, 3, 19, 11, 17, 7, 13]


def getLongList(SIZE):
    """
    Create a list of integers approximately the same number as SIZE
    :param SIZE: integer
    :return: LIST
    """
    NUMBERS = []
    for i in range(2 * SIZE):
        if random.randrange(2) == 1:
            NUMBERS.append(i)
    return NUMBERS


def getRandomList(SIZE):
    """
    Creates a randomized list of integers approximately the same number as SIZE
    :param SIZE: integer
    :return: list
    """
    NUMBERS = getLongList(SIZE)
    random.shuffle(NUMBERS)
    return NUMBERS

