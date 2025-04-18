from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    l = [i for i in range(1,n + 1)]
    password_length = len(q[0])
    
    for c in combinations(l,password_length):
        
        flag = True
        c_set = set(c)
        for query,ans_number in zip(q,ans):
            query_set = set(query)
            
            if len(query_set.intersection(c_set)) != ans_number:
                flag = False
        
        if flag:
            answer+=1
        
    return answer