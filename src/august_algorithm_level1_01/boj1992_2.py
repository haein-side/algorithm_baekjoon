# 동희님 코드

import sys
input = sys.stdin.readline

a = int(input())
board = [list(map(int,input().strip())) for i in range(a)]



def quad_tree(x,y,n) :
    number = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n) :
            if number != board[i][j] :
                #1사분면
                print('(',end='')
                quad_tree(x,y,n//2)

                #2사분면

                quad_tree(x,y+n//2,n//2)

                #3사분면

                quad_tree(x+n//2,y,n//2)

                #4사분면

                quad_tree(x+n//2,y+n//2,n//2)
                print(')',end='')
                return
    if number == 0 :
        print('0',end='')
        return
    else :
        print('1',end='')
        return


quad_tree(0,0,a)