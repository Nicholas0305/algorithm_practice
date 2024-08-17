def binary_search(arr, target):
    low = arr[0]
    high = arr[len(arr) - 1]

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == "__main__":
    arr, target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10
    print(binary_search(arr, target))
