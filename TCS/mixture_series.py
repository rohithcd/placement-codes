'''
Consider the below series:
1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17…..

This series is a mixture of 2 series fail the odd terms in this series form a Fibonacci series and all the even terms are the prime numbers in ascending order

Write a program to find the Nth term in this series

The value N in a positive integer that should be read from mm. The Nth term that is calculated by the program should be written to STDOUT Otherthan the value of Nth term , no other characters / string or message should be written to STDOUT.

For example, when N:14, the 14th term in the series is 17 So only the value 17 should be printed to STDOUT
'''

def solution(n):
    if n % 2 == 0:
        return prime(n/2)
    else:
        return fibo((n+1)/2)
        

def fibo(n, memo={}):
    if n in memo:
        return memo[n]
        
    if n <= 2:
        return 1
        
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

def prime(n):
    num = int(n)
    prime = []
    if num == 1:
        return 2
        
    for i in range(3, num**2):
        print(i)
        if is_prime(i):
            prime.append(i)
            
        if len(prime) == num:
            break
            
    return prime[num-2]
    
    
def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
            
    return True 
    

print(solution(76))
