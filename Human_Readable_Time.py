#!/usr/bin/env python3
'''
https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python


Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''


def make_readable(seconds: int) -> str:
    mm = seconds // 60
    ss = seconds - mm*60
    hh = mm // 60
    mm = mm - hh*60
    return f'{hh:02}:{mm:02}:{ss:02}'


print(make_readable(86399))
print(make_readable(60))


'''
Best Practices
'''
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)



