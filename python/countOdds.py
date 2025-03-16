#  Count the occurrences of the first odd number in an Array
def count_first_odd(arr):
    odd = -1
    for n in arr:
        if n % 2 == 1:
            odd = n
            break

    return arr.count(odd) if odd > -1 else odd

count_first_odd([2, 3, 6, 3, 3, 8, 3])  # 4
count_first_odd([1, 2, 4, 6, 8])  # 1
count_first_odd([2, 4, 6, 8])  # -1

#  The user can choose the odd in an especific position
def count_odd_by_position(arr, pos):
    numbers = []
    for n in arr:
        if n % 2 == 1:
            if len(numbers) != pos:
                numbers.append(n)
            else:
                break
    
    return arr.count(numbers[-1]) if len(numbers) == pos else -1

print(count_odd_by_position([2, 3, 6, 3, 5, 8, 3] , 3))  # 4
print(count_odd_by_position([1, 2, 4, 6, 8] , 2))  # -1
print(count_odd_by_position([2, 4, 6, 8] , 1))  # -1
print(count_odd_by_position([2, 4, 3, 6 , 7 ,9 , 8 , 4 , 7 ] , 2))  # 2