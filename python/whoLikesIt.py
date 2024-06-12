def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return  f'{names[0]} likes this'
    elif len(names) == 2: 
        return  f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
         return  f'{names[0]}, {names[1]} and {names[2]} like this'
    else: 
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]  ))
print(likes(["Max", "John", "Mark"]    ))
print(likes(["Alex", "Jacob", "Mark", "Max"]))

# Expected Output:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

# Couldn't think of any better way to do it :P