def move_zeros(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(0)
    return lst

# [1, 0, 1, 2, 0, 1, 3] returns [1, 1, 2, 1, 3, 0, 0]
# [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(move_zeros([1, 0, 1, 2, 0, 1, 3])) 
print(move_zeros([9, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0] ))