row = 5
b = 0

for i in range(row,0,-1):
    b +=1
    for j in range(1,i+1):
        print('*',end='')
    print('')