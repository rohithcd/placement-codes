def solution(arr, n, k):
    result = []
    
    # If rotation is greater
    # than size of array
    k = k % n
 
    for i in range(n):
 
        if(i < k):

            # Printing rightmost
            # kth elements
            result.append(arr[n + i - k])
 
        else:
 
            # Prints array after
            # 'k' elements
            result.append(arr[i - k])
 
    return result
 
# Driver code
#Example
Array = [ 1, 2, 3, 4, 5 ]
N = len(Array)
K = 5
     
print(solution(Array, N, K))
