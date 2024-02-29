#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if not list_of_integers:
        return None

    lo = 0
    hi = len(list_of_integers) - 1

    while lo < hi:
        mid = (hi + lo) // 2

        if list_of_integers[mid] >= list_of_integers[mid - 1] and \
           list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]

        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1

        else:
            hi = mid - 1

    return list_of_integers[lo]
