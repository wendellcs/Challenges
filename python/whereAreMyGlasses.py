import re
def find_glasses(lst):
    for i in range(len(lst)):
        if(re.search(r'O-+O', lst[i])):
            return i

# Expected output

# ["phone", "O-O", "coins", "keys"] ➞ 1

# ["OO", "wallet", "O##O", "O----O"] ➞ 3

# ["O--#--O", "dustO---Odust", "more dust"] ➞ 1

print(find_glasses(["phone", "O-O", "coins", "keys"]))
print(find_glasses(["OO", "wallet", "O##O", "O----O"]))
print(find_glasses(["O--#--O", "dustO---Odust", "more dust"]))