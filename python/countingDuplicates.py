def duplicate_count(text):
    duplicates = {}
    for l in text.lower(): 
        if(l in duplicates): 
            duplicates[f'{l}'] += 1
        else: 
            duplicates[f'{l}'] = 1

    count = 0
    for i in duplicates.values():
        if i > 1:
            count += 1
    
    return count

# Expected output

# (""), 0)
# ("abcde"), 0)
# ("abcdeaa"), 1)
# ("abcdeaB"), 2)
# ("Indivisibilities"), 2)

print(duplicate_count(""))
print(duplicate_count("abcde"))
print(duplicate_count("abcdeaa"))
print(duplicate_count("abcdeaB"))
print(duplicate_count("Indivisibilities"))