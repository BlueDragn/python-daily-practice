"""
Problem: Reverse an array

My First Attempt (Bug):

I tried reversing the array using pop() and append() inside a for loop.

Bug:
I iterated over the same list that I was modifying.

for i in arr:
    removed = arr.pop()

This caused incorrect results because Python's for loop creates an iterator
based on the original list. When elements are removed during iteration,
the loop stops early.

Example Output:
newArray = [6, 5, 4]
arr = [1, 2, 3]

Correct Insight:
Never modify a list while iterating over it using "for element in list".

Better approaches:
1. Use a while loop
2. Use index-based iteration
3. Use two-pointer swapping

arr = [1,2,3,4,5,6]
newArray = []
#removed = arr.pop()
#newArray.append(removed)
#print(newArray)
for i in arr:
    removed = arr.pop()
    newArray.append(removed)
print(newArray)
print(arr)
"""

arr = [1,2,3,4,5,6]
newArray = []
while arr:
    removed = arr.pop()
    newArray.append(removed)
print(newArray)
print(arr)
"""
Lessons Learned:
- Do not modify a list while iterating over it
- Use while loops when removing elements
"""
