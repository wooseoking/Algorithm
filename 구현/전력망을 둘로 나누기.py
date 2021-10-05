count = 0
def dfs(num_,visited_,graph_):
    global count
    visited_[num_] = True
    count+=1
    for next_ in graph_[num_]:
        if not visited_[next_]:
            dfs(next_,visited_,graph_)

def solution(n, wires):
    global count

    result = []
    for i in range(n-1):
        connect = wires[:i] + wires[i+1:]
        graph = [[] for _ in range(n+1)]
        visited = [False]*(n+1)
        for a,b in connect:
            graph[a].append(b)
            graph[b].append(a)

        first = False
        v1,v2 = -1,-1
        for num in range(1,n+1):
            if not visited[num]:
                count = 0
                dfs(num,visited,graph)
                if not first:
                    first = True
                    v1 = count
                else:v2 = count
        result.append(abs(v1-v2))
    answer = min(result)

    return answer