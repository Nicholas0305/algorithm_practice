def find_product(arr):
    """
    Find the product of the three largest elements in the array.

    Args:
    - arr: List of integers

    Returns:
    - int: Product of the three largest elements
    """
    size = len(arr)
    # Sort the array in ascending order
    for i in range(size):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # Extract the three largest elements
    new_array = arr[-3:]
    product = new_array[0] * new_array[1] * new_array[2]
    return product


def sum_of_all_even_numbers(arr):
    """
    Find the sum of all even numbers in the array.

    Args:
    - arr: List of integers

    Returns:
    - int: Sum of all even numbers
    """
    size = len(arr)
    sum = 0
    # Iterate through the array and add even numbers to the sum
    for i in range(size):
        if arr[i] % 2 == 0:
            sum += arr[i]
    return sum


def count_vowels(str):
    """
    Count the number of vowels in the given string.

    Args:
    - str: Input string

    Returns:
    - int: Number of vowels in the string
    """
    size = len(str)
    sum = 0
    # Iterate through the string and count vowels
    for i in range(size):
        if str[i] in "aeiouAEIOU":
            sum += 1
    return sum


def find_maximum_difference(arr):
    """
    Find the maximum difference between any two elements in the array.

    Args:
    - arr: List of integers

    Returns:
    - int: Maximum difference between any two elements
    """
    size = len(arr)
    max_diff = 0
    # Iterate through the array and calculate differences
    for i in range(size - 1):
        for j in range(i, -1, -1):
            if arr[i] - arr[j] > max_diff:
                max_diff = abs(arr[i] - arr[j])
    return max_diff


def find_longest_contiguous_sub_array(arr):
    """
    Find the length of the longest contiguous subarray of increasing integers.

    Args:
    - arr: List of integers

    Returns:
    - int: Length of the longest contiguous subarray
    """
    size = len(arr)
    if size == 0:
        return 0

    max_length = 1
    current_length = 1
    # Iterate through the array and update current and maximum lengths
    for i in range(size - 1):
        if arr[i] < arr[i + 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1  # Reset current length if not increasing

    return max_length


def two_sum(arr, target):
    """
    Find indices of two numbers in the array that add up to the target.

    Args:
    - arr: List of integers
    - target: Target sum

    Returns:
    - List[int]: Indices of two numbers that add up to the target
    """
    size = len(arr)
    # Iterate through pairs of numbers and check if their sum equals the target
    for i in range(size - 1):
        for j in range(i + 1, size - 1):
            if arr[i] + arr[j] == target:
                return [i, j]
    # Return empty list if no such pair is found
    return []


def two_sum_hash(nums, target):
    """
    Find indices of two numbers in the array that add up to the target using hashing.

    Args:
    - arr: List of integers
    - target: Target sum

    Returns:
    - List[int]: Indices of two numbers that add up to the target
    """
    num_indices = {}
    # Iterate through the array and store indices of numbers
    for i in range(len(nums)):
        num = nums[i]
        diff = target - num
        if diff in num_indices:
            return [num_indices[diff], i]
        else:
            num_indices[num] = i
    # Return empty list if no such pair is found
    return []


def anagrams(str1, str2):
    """
    Check if two strings are anagrams of each other.

    Args:
    - str1: First input string
    - str2: Second input string

    Returns:
    - bool: True if strings are anagrams, False otherwise
    """
    size1 = len(str1)
    size2 = len(str2)
    if size1 == size2:
        for i in range(size1):
            if str1[i] in str2:
                continue
            else:
                return False
        return True
    return False


def anagrams_hash(str1, str2):
    """
    Check if two strings are anagrams of each other using hashing.

    Args:
    - str1: First input string
    - str2: Second input string

    Returns:
    - bool: True if strings are anagrams, False otherwise
    """
    if len(str1) != len(str2):
        return False

    char_freq1 = {}
    char_freq2 = {}

    for char in str1:
        char_freq1[char] = char_freq1.get(char, 0) + 1

    for char in str2:
        char_freq2[char] = char_freq2.get(char, 0) + 1

    return char_freq1 == char_freq2


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    print(two_sum_hash(arr, 10))
