import sys
import heapq
import math
from collections import deque
import bisect
from itertools import *
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

row,col = map(int,input().split())
board = []
for _ in range(row):
    board.append(input().strip())

max_k = min(row,col)

arr = []
Area = []
for i in range(0,8):
    arr.append(i)
    Area.append(4*i+1)

comb_list = list(combinations_with_replacement(arr,2))

ans = 1

def inside(y,x):
    return 0<=y<row and 0<=x<col


def check(i,j,size,visits):
    if board[i][j]!="#":return False
    if visits[i][j]:return False
    for k in range(4):
        ny = i
        nx = j
        for _ in range(size):
            ny+=dy[k]
            nx+=dx[k]
            if not inside(ny,nx):return False
            if visits[ny][nx]:return False
            if board[ny][nx]!="#":return False
    return True

def visit(i,j,size,c):
    c[i][j] = True
    for k in range(4):
        ny = i
        nx = j
        for _ in range(size):
            ny += dy[k]
            nx += dx[k]
            c[ny][nx] = True

def de_visit(i,j,size,c):
    c[i][j] = False
    for k in range(4):
        ny = i
        nx = j
        for _ in range(size):
            ny += dy[k]
            nx += dx[k]
            c[ny][nx] = False


def go(size1,size2):
    U = [i for i in range(0,row*col)]
    U_comb = list(combinations(U,2))

    for ele1,ele2 in U_comb:
        y1 = ele1//col
        x1 = ele1%col
        y2 = ele2//col
        x2 = ele2%col
        visited = [[False] * col for _ in range(row)]
        if check(y1,x1,size1,visited):
            visit(y1,x1,size1,visited)
            if check(y2,x2,size2,visited):
                return True
    return False

# 크기 두개의 십자가에대해서 가능?
for first,second in comb_list:
    if go(first,second) or go(second,first):
        ans = max(ans,Area[first]*Area[second])

print(ans)
