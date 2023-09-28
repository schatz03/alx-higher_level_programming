#!/usr/bin/python3
"""Defines a peak-finding algorithm"""


def find_peak(list_of_integers):
    """ Finds the peak in a list of integers """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    n = int(length / 2)
    li = list_of_integers

    if n - 1 < 0 and n + 1 >= length:
        return li[n]
    elif n - 1 < 0:
        return li[n] if li[n] > li[n + 1] else li[n + 1]
    elif n + 1 >= length:
        return li[n] if li[n] > li[n - 1] else li[n - 1]

    if li[n - 1] < li[n] > li[n + 1]:
        return li[n]

    if li[n + 1] > li[n - 1]:
        return find_peak(li[n:])
    return find_peak(li[:n])
