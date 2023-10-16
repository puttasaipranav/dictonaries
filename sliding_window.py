def sliding_window(arr, k):
    n = len(arr)
    if n < k:
        return []

    result = []
    for i in range(n - k + 1):
        window = arr[i:i + k]
        result.append(window)
    
    return result

# Example usage:

window_size = 3

windows = sliding_window(my_list, window_size)
print("Sliding Windows:")
for window in windows:
    print(window)