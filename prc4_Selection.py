# Create an empty list
arr = []

# Take number of elements from user
n = int(input("Enter number of elements: "))

# Input elements from user
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

# Selection Sort Logic
for i in range(n):

    # Assume current index has minimum value
    min_index = i

    # Find the smallest element in remaining array
    for j in range(i + 1, n):

        # Compare elements
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap smallest element with current element
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Display sorted array
print("Sorted Array:")
print(arr)
