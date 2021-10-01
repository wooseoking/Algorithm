import sys
input = sys.stdin.readline
tree = [-1]

def preorder(idx,cnt):
    if idx>length//2:return
    arr[cnt] = tree[idx]
    print(idx,tree[idx])
    preorder(2*idx,cnt+1)
    preorder(2*idx+1,cnt+1)

try:
    while True:
        n = int(input())
        tree.append(n)
except:
    length = len(tree)
    arr = [-1] * length
    preorder(1,0)