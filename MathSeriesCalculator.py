# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 18:28:05 2019

@author: Jay
"""

"""
 TITLE: Math series calculator
 VERSION: Nil
 CREATED: 2019
 AUTHOR: GREER, J
 
 DESCRIPTION:
 Created to assist me with math homework. This program is given a series and will calculate it's first couple of answers so I can see it.
 """
#Variables
start = 5
end = start + 50

#Math Variables
e = 2.71828182846
pi = 3.14159265359


def series(k): #** is to the power of
    ans = (e**k) / (pi **k)
    return (k,round(ans,5))

#Test function for specific value of K. Called T instead of Test because it's shorter.
def t(k):
    answer = series(k)
    print("k = {}: {}".format(answer[0], answer[1]))


for k in range(start, end):
    answer = series(k)
    print("k = {}: {}".format(answer[0], answer[1]))
    