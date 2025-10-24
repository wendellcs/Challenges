def staircase(n):
    stair = []
    iteration = 0
    for i in range(n):
        row = ''
        for j in range(n):
            row += '#'
            
        for k in range(iteration):    
            row = row.replace('#', ' ', 1)
        
        iteration += 1
        stair.append(row)
   
    print('\n'.join(stair[::-1]))

staircase(8)