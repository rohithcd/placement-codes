N = int(input())
elements = list(map(int , input().split(' ')))
sub, size = [], len(elements)
elements.sort()

def split(arr, k):
  return arr[:k], arr[k:]

def diff(arr):
  return arr[0] if len(arr) == 1 else max(arr) - min(arr)
  
for i in range(1, size):
  arr1, arr2 = split(elements, i)
  sub.append(abs(diff(arr1) - diff(arr2)))

print(min(sub))
  



  



