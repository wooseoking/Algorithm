import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
n = int(input())
w = [list(map(int,input().split())) for _ in range(n)]
print(w)