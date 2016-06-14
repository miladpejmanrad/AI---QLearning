import random
import copy

print 'Please note that I chose 4 for the Q-value of the Pizza place and 40 for Q-value of the Goal\n'
M = [ # The main grid [Reward, Left, Right, Up, Down, Up-left, Up-right]
    
    [[-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0],
     [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0],
     [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
     [-1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
     [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
     [-1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [40, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0], [4, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0]],
    
    [[-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0],
     [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0],
     [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0]],
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
    if i>0 and j>0:
        choices.append([i-1, j-1, 5]) # Up-Left
    if i>0 and j<14:
        choices.append([i-1, j+1, 6]) # Up-Right
    return random.choice(choices)


def which(i,j): # returns the maximum Q-value of the current state. Useful for printing the path from S to P to G
    m = max(M[i][j][1:])
    for x in range(1,7):
        if M[i][j][x] == m:
            if x == 1 and j > 0:
                return [i, j-1, m]
            if x == 2 and j < 14:
                return [i, j+1, m]
            if x == 3 and i > 0:
                return [i-1, j, m]
            if x == 4 and i < 8:
                return [i+1, j, m]
            if x == 5 and i > 0 and j > 0:
                return [i-1, j-1, m]
            if x == 6 and i > 0 and j < 14:
                return [i-1, j+1, m]
            
discount = input('''Please enter the discount value:
    ''')  


learning = input('''Please enter the learning value:
    ''')


for index in range(100):
    i = 2
    j = 12
    f = 0 # flag for making sure that Pizza place is traveresed 
    while (True):
        data = pick(i,j)
        ii = data[0]
        jj = data[1]
        direction = data[2]
        if i == 6 and j == 2 and f == 1:
            M[i][j][direction] = (1-learning) * M[i][j][direction] + learning * M[i][j][0]
            break
        if i == 6 and j == 2 and f == 0: 
            M[i][j][direction] = (1-learning) * M[i][j][direction] + learning * M[i][j][0]
            i = ii
            j = jj
            continue
        M[i][j][direction] = (1-learning) * M[i][j][direction] + learning * (M[i][j][0] + discount * max(M[ii][jj][1:]))
        if i == 7 and j == 6:
            f = 1
        i = ii
        j = jj

p = copy.deepcopy(M)
i = 2
j = 12
counter = 0
while (True):
    data = which(i,j)
    p[i][j] = data[2]
    if i == 6 and j == 2:
        break
    i = data[0]
    j = data[1]
    counter += 1
    if counter > 1000:
        print 'You stuck in an infinite loop! Please try different values for learning and discount!'
        break
if counter < 1000:
    print '\nThe path from Start to Pizza place and then to Goal:'
    for row in p:
        for val in row:
            if type(val) == float:
                print '{:8}'.format('%.3f'%(val)),
            else:
                print '{:8}'.format(""), # Values are truncated by '%.3f'% for the sake of demonstration
        print


    for i in range(1,7):
        if i == 1:
            s = 'left'
        elif i == 2:
            s = 'right'
        elif i == 3:
            s = 'up'
        elif i == 4:
            s = 'down'
        elif i == 5:
            s = 'up-left'
        else:
            s = 'up-right'
        print "The {} Q-values of each state:".format(s)
        for row in M:
            for lst in row:
                print '{:7}'.format('%.3f'%(lst[i])), # Values are truncated by '%.3f'% for the sake of demonstration
            print
        print
        print