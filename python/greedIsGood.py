def score(dice):
    value = 0
    value2 = 0
    for item in [{f'{n}':dice.count(n)} for n in dice]:
        key = int(list(item)[0])
        if item[str(key)] >= 3:
            rest = item[str(key)] - 3
            if key == 5 or key == 1:
                value = key * 100 + rest * 50 if key != 1 else key * 1000 + rest * 100
            else:
                value = key * 100 if key != 1 else key * 1000
        else:
            if key == 5 or key == 1:
                value2 += 50 if key == 5 else 100

    return value + value2
         
# Three 1's => 1000 points
# Three 6's =>  600 points
# Three 5's =>  500 points
# Three 4's =>  400 points
# Three 3's =>  300 points
# Three 2's =>  200 points
# One   1   =>  100 points
# One   5   =>   50 points

print(score( [5, 1, 3, 4, 1])) # 250
print(score( [1, 1, 1, 2, 1])) # 1100
print(score( [1, 1, 1, 1, 5])) # 1150
print(score( [5, 5, 5, 5, 6])) # 550
print(score( [2, 4, 4, 5, 4])) # 450
print(score( [2, 3, 4, 6, 2])) # 0
print(score( [4, 4, 4, 3, 3])) # 400
print(score( [2, 4, 4, 5, 4])) # 450
