#approach1
arr = [4,2,9,1,7]
max_element = arr[0]
for num in arr:
    if num < max_element:
        max_element = num
print(max_element)