def staircase(n):
    stair = ''
    iteration = 0
    for i in range(n):
        row = ''
        for j in range(n):
            row += '#'
            
        for k in range(iteration):    
            row = row.replace('#', ' ', 1)
        
        iteration += 1
        stair += '\n'.join(row)
   
    print(stair)

staircase(8)