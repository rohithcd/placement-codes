'''
Given Two Non-Negative Integers N1 And N2, Where N1 < N2. 
The Task Is To Find The Total Number Of Integers In the range Interval [N1, N2] 
'''
#My solution
def solution(n1, n2):
    count = 0 
    
    for i in range(n1, n2 + 1):
        if check_digit(i):
            count += 1 
            
    return count 
    
def check_digit(i):
    item = str(i)
    length = len(item)
    
    return len(set(item)) == len(item)
    
# Driver code
#Example
n1 = 101
n2 = 200
     
print(solution(n1, n2))


#From GeeksForGeeks
# Function to check if the given
# number has repeated digit or not
def repeated_digit(n):
    a = []
     
    # Traversing through each digit
    while n != 0:
        d = n%10
         
        # if the digit is present
        # more than once in the
        # number
        if d in a:
             
            # return 0 if the number
            # has repeated digit
            return 0
        a.append(d)
        n = n//10
     
    # return 1 if the number has no
    # repeated digit
    return 1
 
# Function to find total number
# in the given range which has
# no repeated digit
def calculate(L,R):
    answer = 0
     
    # Traversing through the range
    for i in range(L,R+1):
         
        # Add 1 to the answer if i has
        # no repeated digit else 0
        answer = answer + repeated_digit(i)
     
    # return answer
    return answer
     
# Driver's Code
L=1
R=100
 
# Calling the calculate
print(calculate(L, R))
