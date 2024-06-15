def count(s):
    result = {}
    for c in s:
        if c in result:
            result[f'{c}'] += 1
        else:
            result[f'{c}'] = 1
    return result

# 'aba' ---> {'a': 2, 'b': 1}.

print(count('aba'))