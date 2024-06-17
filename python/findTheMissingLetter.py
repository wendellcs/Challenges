import string
def find_missing_letter(chars):
    alphabet = string.ascii_letters
    index = []
    for i in range(len(chars)):
        index.append(alphabet.index(chars[i]))

    for i in range(len(index)):
        if (index[i] + 1) != index[i + 1]:
            return alphabet[index[i] + 1]
        
# Expected output
# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'

print(find_missing_letter(['a','b','c','d','f']))
print(find_missing_letter(['O','Q','R','S']))