def solution(s):
    if len(s) % 2 == 1:
        s += '_'

    res = []

    for i in range(0 , len(s) , 2):
        res.append(s[i : i + 2])

    return res


# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

print(solution('abc'))
print(solution('abcdef'))