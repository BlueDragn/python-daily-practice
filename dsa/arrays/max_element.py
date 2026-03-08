#approach1
arr = [4,2,9,1,7]
max_element = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]
print(max_element)

#approach2
arr = [4,2,9,1,7]
max_element = arr[0]
for num in arr:
    if num > max_element:
        max_element = num
print(max_element)