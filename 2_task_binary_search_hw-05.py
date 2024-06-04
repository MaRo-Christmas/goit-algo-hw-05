
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == x:
            return (iterations, arr[mid])
        elif arr[mid] < x:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]
        
    return (iterations, upper_bound)

# Приклад використання:
sorted_array = [0.1, 0.5, 1.3, 3.7, 4.2, 6.9, 7.1, 9.3, 10.5]
value_to_search = 5.0

result = binary_search(sorted_array, value_to_search)
print(result)  # Кількість ітерацій, верхня межа
