"""
This is a binary search program
this is to search for a number from a list
using devide and find method
"""

def binary_search(n, arr):
    start = 0
    step = 0
    stop = len(arr)-1

    while start <= stop:
        mid = (start + stop)//2
        if n == arr[mid]:
            return f"{n} found in {arr} at {mid}"
        elif n < arr[mid]:
            stop = mid-1
        else:
            start = mid+1
    print(start, stop)
    return "not found"

def list_generator(max_val):
    arr = []
    for num in range(1,max_val+1):
        arr.append(num)
    return arr

print(binary_search(2, list_generator(100)))
