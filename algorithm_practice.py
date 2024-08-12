def find_product(arr):
    size = len(arr)
    for i in range(size):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    new_array = arr[-3:]
    product = new_array[0] * new_array[1] * new_array[2]
    return product


def sum_of_all_even_numbers(arr):
    total = 0
    for i in arr:
        if i % 2 == 0:
            total += i
    return total


def count_vowels(s):
    total = 0
    for i in s:
        if i in "aeiouAEIOU":
            total += 1
    return total


def find_maximum_difference(arr):
    max_diff = 0
    for i in range(len(arr) - 1):
        for j in range(i):
            if arr[i] - arr[j] > max_diff:
                max_diff = arr[i] - arr[j]
    return max_diff


def find_longest_contiguous_sub_array(arr):
    if not arr:
        return 0

    max_length = 1
    current_length = 1
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length


def two_sum(arr, target):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []


def two_sum_hash(nums, target):
    num_indices = {}
    for i in range(len(nums)):
        num = nums[i]
        diff = target - num
        if diff in num_indices:
            return [num_indices[diff], i]
        num_indices[num] = i
    return []


def anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in str1:
        if i not in str2:
            return False
    return True


def anagrams_hash(str1, str2):
    if len(str1) != len(str2):
        return False

    char_freq1 = {}
    char_freq2 = {}

    for char in str1:
        char_freq1[char] = char_freq1.get(char, 0) + 1

    for char in str2:
        char_freq2[char] = char_freq2.get(char, 0) + 1

    return char_freq1 == char_freq2


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_elements(list1, list2):
    return [i for i in list1 if i in list2]


def remove_duplicates(lst):
    cache = {}
    result = []
    for item in lst:
        if item not in cache:
            result.append(item)
            cache[item] = True
    return result


def word_count(s):
    words = s.split()
    cache = {}
    for word in words:
        cache[word] = cache.get(word, 0) + 1
    return cache


def longest_common_prefix(array):
    prefix = array[0]
    for word in array[1:]:
        i = 0
        while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
            i += 1
        prefix = prefix[:i]
    return prefix


def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    longest = ""
    for i in range(len(s)):
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1

        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest


if __name__ == "__main__":
    s = "babad"
    print(longest_palindrome(s))
