import random
import copy

M = [ # The main grid [Reward, Left, Right, Up, Down]
    
    [[-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0],
     [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0],
     [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [-1, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [-1, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [-1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
     [-1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [-1, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
     [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
     [-1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [-1, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [3, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [-1, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [-1, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0],
     [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0],
     [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0]],
]

def pick(i,j): # randomly returns one of the neighbours of the current state
    choices = []
    if i>0:
        choices.append([i-1, j, 3]) # Up
    if i<8:
        choices.append([i+1, j, 4]) # Down
    if j>0:
        choices.append([i, j-1, 1]) # Left
    if j<14:
        choices.append([i, j+1, 2]) # Right
    return random.choice(choices)


def which(i,j): # returns the maximum Q-value of the current state. Useful for printing the path from S to G
    m = max(M[i][j][1:])
    for x in range(1,5):
        if M[i][j][x] == m:
            if x == 1 and j > 0:
                return [i, j-1, m]
            if x == 2 and j < 14:
                return [i, j+1, m]
            if x == 3 and i > 0:
                return [i-1, j, m]
            if x == 4 and i < 8:
                return [i+1, j, m]
            
discount = input('''Please enter the discount value:
    ''')          

learning = input('''Please enter the learning value:
    ''')


for index in range(1000):
    i = 2
    j = 12
    while (True):
        data = pick(i,j)
        ii = data[0]
        jj = data[1]
        direction = data[2]
        if i == 6 and j == 2:
            M[i][j][direction] = (1-learning) * M[i][j][direction] + learning * M[i][j][0]
            break
        M[i][j][direction] = (1-learning) * M[i][j][direction] + learning * (M[i][j][0] + discount * max(M[ii][jj][1:]))
        i = ii
        j = jj
        

p = copy.deepcopy(M)
i = 2
j = 12
while (True):
    data = which(i,j)
    p[i][j] = data[2]
    if i == 6 and j == 2:
        break
    i = data[0]
    j = data[1]

print '\nThe path from Start to Goal:'
for row in p:
    for val in row:
        if type(val) == float:
            print '{:8}'.format('%.3f'%(val)), # Values are truncated by '%.3f'% for the sake of demonstration
        else:
            print '{:8}'.format(""),
    print
    
    
for i in range(1,5):
    if i == 1:
        s = 'left'
    elif i == 2:
        s = 'right'
    elif i == 3:
        s = 'up'
    else:
        s = 'down'
    print "The {} Q-values of each state:".format(s)
    for row in M:
        for lst in row:
            print '{:7}'.format('%.3f'%(lst[i])), # Values are truncated by '%.3f'% for the sake of demonstration
        print
    print
    print