#!/usr/bin/env python3
'''
Back and forth then Reverse!
https://www.codewars.com/kata/60cc93db4ab0ae0026761232/train/python

Task
A list S will be given. You need to generate a list T from it by following the given process:

Remove the first and last element from the list S and add them to the list T.
Reverse the list S
Repeat the process until list S gets emptied.
The above process results in the depletion of the list S. Your task is to generate list T without mutating the input List S.

Example
S = [1,2,3,4,5,6]
T = []

S = [2,3,4,5] => [5,4,3,2]
T = [1,6]

S = [4,3] => [3,4]
T = [1,6,5,2]

S = []
T = [1,6,5,2,3,4]
return T
Note
size of S goes up to 10^6
Keep the efficiency of your code in mind.
Do not mutate the Input.

'''


# def arrange(s: list) -> list:
#     # Code and make sure not to mutate s!!
#     ss = s.copy()
#     t = []
#     while ss != []:
#         t.append(ss.pop(0))
#         if s != []:
#             t.append(ss.pop())
#
#         if len(ss) > 1:
#             ss.reverse()
#
#     return t
#
#
def arrange(s: list) -> list:
    # Code and make sure not to mutate s!!
    ss = s.copy()
    t = []
    temp = []
    for i in range(len(ss)):
        if len(ss) > 1:
            if i % 2 == 0:
                t.append(ss.pop(0))
                t.append(ss.pop())
            else:
                temp.append(ss.pop(0))
                temp.append(ss.pop())
                temp.reverse()
                t += temp
                temp = []
        elif ss != []:
            t.append(ss.pop())

    return t


print(arrange([5, 6, 7, 8, 9]))




