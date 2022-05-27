# -*- coding: utf-8 -*-
"""
Created on Fri May 27 13:07:12 2022

@author: Raima
"""

n_terms = int(input("Please enter the number of terms required:"))
n1 = 0
n2 = 1
x = 0
if n_terms <= 0:
    print(" Please enter a positive integer only")
elif n_terms == 1:
    print("Fibonacci Sequence upto :",n_terms)
    print(n1)
else :
    print("The Fibonacci Sequence is:")
    while x < n_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth 
        x += 1
          
    