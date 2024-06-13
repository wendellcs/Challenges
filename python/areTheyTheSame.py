def comp(a, b):    
    if (a is None or b is None) or len(a) != len(b):
        return False

    freq_a, freq_b = {}, {}

    for num in [num * num for num in a]:
        if num in freq_a:
            freq_a[num] += 1
        else: 
            freq_a[num] = 1

    for num in b:
        if num in freq_b:
            freq_b[num] += 1
        else: 
            freq_b[num] = 1

    return freq_a == freq_b
    



print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]  ))

# Expected output: True
# a = [121, 144, 19, 161, 19, 144, 19, 11]  
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]  ))

# Expected output: False
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]

