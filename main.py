import random
def printf(showboard):
    for i in range(10):
        print(i,end='')
    print('')
    for i in range(1,10):
        print(i,end='')
        for j in range(1,10):
            print(showboard[i][j],end='')
        print('')
def set(board):
    for i in range(10):
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        board[x][y]=1
def a_board(board,showboard,x,y):
    if 1 <= x <= 9 and 1 <= y <= 9 and board[x][y] == 0:
        c = 0
        for i in range(-1, 2):
            c+= board[x - 1][y+i] + board[x][y+i] + board[x + 1][y+i]
        showboard[x][y]=c
        j=random.randint(-1,1)
        a_board(board,showboard,x+j,y+j)






def game():
    board=[[0]*11 for i in range(11)]
    showboard=[['*']*11 for i in range(11)]
    printf(showboard)
    set(board)
    #printf(board)
    count=0
    count2=0
    while 1:
        if count==71 or count2==10:
            print('游戏成功')
            break

        a = input('a 扫雷  b 排雷')
        if a == 'a':
           x=int(input('请输入行'))
           y=int(input('请输入列'))
           if 1 <= x <= 9 and 1 <= y <= 9 and board[x][y] == 0:
               a_board(board, showboard, x, y)
               printf(showboard)
               count+=1
           elif 1 <= x <= 9 and 1 <= y <= 9 and board[x][y] == 1:
               print('游戏失败')
               break
           else:
               print('请重新选择')
        elif a == 'b':
            x = int(input('请输入行'))
            y = int(input('请输入列'))
            if 1 <= x <= 9 and 1 <= y <= 9 and board[x][y] == 1:
                showboard[x][y]='&'
                printf(showboard)
                count2+= 1
            elif 1 <= x <= 9 and 1 <= y <= 9 and board[x][y] == 0:
                print('游戏失败')
                break
            else:
                print('请重新选择')
        else:
            print('请重新选择')

while 1:
    print('-------------')
    print('---1 play----')
    print('---0 exit----')
    print('-------------')
    a=int(input('请选择'))
    if a==1:
        game()
    elif a==0:
        break
    else:
        print('请重新输入')