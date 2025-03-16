# Verifys if a numeric array is a palindrome

def is_palindrome(arr):
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - i - 1]:
            return False
    return True

print(is_palindrome([1, 2, 3, 2, 1]))  # True
print(is_palindrome([4, 5, 6, 5, 4]))  # True
print(is_palindrome([1, 2, 3, 4, 5]))  # False