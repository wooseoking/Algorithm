import sys
from itertools import *
input = sys.stdin.readline
INF = 1e9

n = int(input())
population = [0] + list(map(int,input().split()))
a = [[] for _ in range(n+1)]
for i in range(1,n+1):
    info = list(map(int,input().split()))
    for nodes in info[1:]:
        a[i].append(nodes)
        a[nodes].append(i)

nodes = [i for i in range(1,n+1)]
U = []
for sel in range(1,n):
    U.append(list(combinations(nodes,sel)))


def dfs(now,group,visited,Color,num):
    if visited[now]:return
    visited[now] = True
    Color[now] =num
    for next_ in a[now]:
        if next_ in group:
            dfs(next_,group,visited,Color,num)

def Go(g_A,g_B):
    population_a = 0
    population_b = 0
    for v in g_A:
        population_a+=population[v]
    for v in g_B:
        population_b+=population[v]

    a_start = g_A[0]
    b_start = g_B[0]
    visited = [False]*(n+1)
    Color = [0]*(n+1)
    dfs(a_start,g_A,visited,Color,1)
    dfs(b_start,g_B,visited,Color,2)

    a_ok = True
    b_ok = True

    for v in range(1,n+1):
        if v in g_A and Color[v]!=1: a_ok = False
        if v in g_B and Color[v]!=2: b_ok = False

    if a_ok and b_ok: return abs(population_a-population_b)
    else : return -1

res = []
for S in U:
    for groupA in S:
        A = list(groupA)
        B = [v for v in nodes if v not in groupA]
        #모든 그룹 나눔
        temp = Go(A,B)
        if temp!=-1:res.append(temp)
if len(res) == 0: print(-1)
else : print(min(res))