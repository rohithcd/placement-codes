'''
Problem Statement -: In this even odd problem Given a range [low, high] (both inclusive), select K numbers from the range (a number can be chosen multiple times) such that sum of those K numbers is even.
Calculate the number of all such permutations.
'''

from itertools import product

def solution(low, high, k):
    items = 0
    values = tuple(i for i in range(low, high+1))
    
    perm = product(values, repeat=k)
    
    for i in tuple(perm):
        if check_even(i):
            items += 1
            
    return items


def check_even(tup):
    return sum(tup) % 2 == 0
    
    
print(solution(1, 10, 2))
