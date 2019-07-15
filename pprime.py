"""
ID: jameshu1
LANG: PYTHON3
TASK: pprime
"""

import sys
from math import sqrt
import array

sys.stdin = open('pprime.in', 'r')
sys.stdout = open('pprime.out', 'w')


def make_bit_array(bit_size, fill=0):
    int_size = bit_size >> 5
    if bit_size & 31:
        int_size += 1
    if fill == 1:
        fill = 4294967295
    else:
        fill = 0
    bit_array = array.array('I')
    bit_array.extend((fill,) * int_size)
    return bit_array


def test_bit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    return array_name[record] & mask


def clear_bit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = ~(1 << offset)
    array_name[record] &= mask
    return array_name[record]


def toggle_bit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    array_name[record] ^= mask
    return array_name[record]


def atkin(limit):
    plist = make_bit_array(limit + 1)

    xx3 = 3
    for dxx in range(0, 12 * int(sqrt((limit - 1) / 3)), 24):
        xx3 += dxx
        y_limit = int(12 * sqrt(limit - xx3) - 36)
        n = xx3 + 16
        for dn in range(-12, y_limit + 1, 72):
            n += dn
            toggle_bit(plist, n)

        n = xx3 + 4
        for dn in range(12, y_limit + 1, 72):
            n += dn
            toggle_bit(plist, n)

    xx4 = 0
    for dxx4 in range(4, 8 * int(sqrt((limit - 1) / 4)) + 4, 8):
        xx4 += dxx4
        n = xx4 + 1

        if xx4 % 3:
            for dn in range(0, 4 * int(sqrt(limit - xx4)) - 3, 8):
                n += dn
                toggle_bit(plist, n)

        else:
            y_limit = 12 * int(sqrt(limit - xx4)) - 36

            n = xx4 + 25
            for dn in range(-24, y_limit + 1, 72):
                n += dn
                toggle_bit(plist, n)

            n = xx4 + 1
            for dn in range(24, y_limit + 1, 72):
                n += dn
                toggle_bit(plist, n)

    xx = 1
    for x in range(3, int(sqrt(limit / 2)) + 1, 2):
        xx += 4 * x - 4
        n = 3 * xx

        if n > limit:
            min_y = ((int(sqrt(n - limit)) >> 2) << 2)
            yy = min_y * min_y
            n -= yy
            s = 4 * min_y + 4

        else:
            s = 4

        for dn in range(s, 4 * x, 8):
            n -= dn
            if n <= limit and n % 12 == 11:
                toggle_bit(plist, n)

    xx = 0
    for x in range(2, int(sqrt(limit / 2)) + 1, 2):
        xx += 4 * x - 4
        n = 3 * xx

        if n > limit:
            min_y = ((int(sqrt(n - limit)) >> 2) << 2) - 1
            yy = min_y * min_y
            n -= yy
            s = 4 * min_y + 4

        else:
            n -= 1
            s = 0

        for dn in range(s, 4 * x, 8):
            n -= dn
            if n <= limit and n % 12 == 11:
                toggle_bit(plist, n)

    for n in range(5, int(sqrt(limit)) + 1, 2):
        if test_bit(plist, n):
            for k in range(n * n, limit, n * n):
                clear_bit(plist, k)

    return [2, 3] + list(filter(lambda xxx: test_bit(plist, xxx), range(5, limit, 2)))


a, b = map(int, input().split())

if a > b // 2:
    primes = atkin(int(sqrt(b)) + 1)
    for nn in range(a, b + 1):
        if str(nn) == str(nn)[::-1]:
            for p in primes:
                if nn == p:
                    print(nn)
                    break
                if not nn % p:
                    break
            else:
                print(nn)
else:
    primes = atkin(b)
    for p in primes:
        if p < a:
            continue
        if str(p) == str(p)[::-1]:
            print(p)
