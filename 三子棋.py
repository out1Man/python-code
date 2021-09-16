import random


def showboard(m,n,b):
    i=j=0
    for i in range(m):
        for j in range(n):
            print(b[i][j] ,end='')
            if j<n-1:
                print('|',end='')
        print('')
        j=0
        if i<m-1:
            for j in range(n):
                print('-', end=' ')
            print(' ')

def playmove(m,n,b):
    while 1:
        print('玩家下棋')
        x = int(input('请选择下棋坐标第几行'))
        y = int(input('请选择下棋坐标第几列'))
        if  1<=x<=3 and 1<=y<=3 and b[x-1][y-1] == 0 :
            b[x-1][y-1] = '#'
            showboard(m, n, b)
            print('')
            break
        else:
            print('请重新输入')

def computermove(m,n,b):

    while 1:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if b[x][y]==0:
            b[x][y]='&'
            print('电脑下棋')
            showboard(m, n, b)
            print('')
            break

def judge(m,n,b):
    for i in range(m):
        if b[i][0]==b[i][1]==b[i][2]:
            return b[i][0]
        if b[0][i]==b[1][i]==b[2][i]:
            return b[0][i]
        if b[0][0]==b[1][1]==b[2][2]:
            return b[0][0]
        if b[2][0]==b[1][1]==b[0][2]:
            return b[1][1]

def game(m,n):
    b=[[0 for i in range(m)]for i  in range(n)]
    showboard(m,n,b)
    while 1:
        playmove(m,n,b)
        judg=judge(m,n,b)
        if judg=='#':
            print("游戏成功")
            break
        computermove(m,n,b)
        judg=judge(m,n,b)
        if judg=='&':
            print("游戏失败")
            break
while 1:
    print('----------------')
    print('-----1 play-----')
    print('-----0 exit-----')
    print('----------------')
    a = int(input('请选择'))
    if a == 1:
        game(3,3)
    elif a==0:
        break
    else:
        print('请重新选择')