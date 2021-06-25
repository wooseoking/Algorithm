if __name__ =="__main__":
    n, m = map(int, input().split())
    image = [list(map(int, input().split())) for _ in range(n)]
    group = [[-1] * m for _ in range(n)]
    table = dict()
    group_num = 1
    parent = [v for v in range(n*m+1)]

    #첫번째
    for i in range(n):
        for j in range(1,m):
            if image[i][j]==0:continue
            if i==0:
                if group[i][j-1]!=-1:
                    group[i][j] = group[i][j-1]
                else:
                    group[i][j] = group_num
                    group_num+=1
            else:
                top_y ,top_x = i-1,j
                left_y,left_x = i,j-1
                t = image[top_y][top_x]
                l = image[left_y][left_x]
                if t==0 and l==0:
                    group[i][j] = group_num
                    group_num+=1
                if t==0 and l == 1 or t==1 and l==0:
                    if l==1:
                        group[i][j] = group[left_y][left_x]
                    elif t==1:
                        group[i][j] = group[top_y][top_x]
                if t==1 and l==1:
                    group[i][j] = group[top_y][top_x]
                    if group[top_y][top_x] != group[left_y][left_x]:
                        if group[top_y][top_x] < group[left_y][left_x]:
                            parent[group[left_y][left_x]] = group[top_y][top_x]
                        else:
                            parent[group[top_y][top_x]] = group[left_y][left_x]
    #두번째 더 작은 원소로 맵핑 하진 않음
    for i in range(n):
        for j in range(m):
            if group[i][j]==-1:print(0,end=' ')
            else:print(group[i][j],end=' ')
        print()