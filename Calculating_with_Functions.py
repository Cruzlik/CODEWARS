#!/usr/bin/env python3
'''

https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/python

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
'''


def _digit(number: int, operator=None):
    if operator is None:
        return number
    return operator(number)

def zero(operator=None) -> int:
    return _digit(0, operator)

def one(operator=None) -> int:
    return _digit(1, operator)

def two(operator=None) -> int:
    return _digit(2, operator)

def three(operator=None) -> int:
    return _digit(3, operator)

def four(operator=None) -> int:
    return _digit(4, operator)

def five(operator=None) -> int:
    return _digit(5, operator)

def six(operator=None) -> int:
    return _digit(6, operator)

def seven(operator=None) -> int:
    return _digit(7, operator)

def eight(operator=None) -> int:
    return _digit(8, operator)

def nine(operator=None) -> int:
    return _digit(9, operator)

def times(second_operand: int):
    return lambda first_operand: first_operand * second_operand

def plus(second_operand: int):
    return lambda first_operand: first_operand + second_operand

def minus(second_operand: int):
    return lambda first_operand: first_operand - second_operand

def divided_by(second_operand: int):
    return lambda first_operand: int(first_operand / second_operand)

'''
BEST
'''
def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y