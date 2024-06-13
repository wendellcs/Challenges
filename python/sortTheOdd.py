def sort_array(sa):
    result, even = [], []

    for index, item in enumerate(sa):
        if item % 2 == 1:
            result.append(item)
        else:
            even.append((index, item))

    result.sort()

    for item in range(len(even)): 
        result.insert(even[item][0], even[item][1])

    return result

# Expected output

# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
# [-14, -43, -31, -8, -29, -8, 28, 23, -40, 28, 36, 32, 35, -14, 30, 16, 45, 47]
# [0, -39, -2, 42, -21, 8, -1, 40, 16, -38, 15, 19, 50, 23, 36, -18, 29, -32, 2, 31, -44, 48, 8, -34, 41, 16, 43]

print(sort_array([7 ,1]))
print(sort_array([5, 8, 6, 3, 4]))
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
print(sort_array([-14, -43, -31, -8, -29, 23, 28, 35, -40, 45, 36, 32, 47, 30, 16] ))
print(sort_array([0, -39, -2, 42, -21, 8, -1, 40, 16, -38, 15, 19, 50, 23, 36, -18, 29, -32, 2, 31, -44, 48, 41, -34, 43]))
