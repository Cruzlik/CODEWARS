#!/usr/bin/env python3
'''
https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python

Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8

'''


def row_sum_odd_numbers(n):
    # your code here
    if n == 1: return 1
    p = n**2 - (n -1)
    summ = 0
    for i in range(n):
        summ += p + i * 2
    return summ

print(row_sum_odd_numbers(13))

'''
BEST 
'''
def row_sum_odd_numbers(n):
    #your code here
    return n ** 3