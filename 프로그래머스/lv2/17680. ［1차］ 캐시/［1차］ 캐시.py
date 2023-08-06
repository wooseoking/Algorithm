from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    n = len(cities)
    HITTIME = 1
    MISSTIME = 5

    #EdgeCase
    if cacheSize == 0:
        return n * MISSTIME

    for i in range(n):
        cities[i] = cities[i].lower()

    for city in cities:
        #캐시 히트 , cache 제일 왼쪽이 최신
        if city in cache:
            answer += HITTIME
            cache.remove(city)
            cache.appendleft(city)
        else:
            answer += MISSTIME
            
            if len(cache) < cacheSize:
                cache.appendleft(city)
            else:
                cache.pop()
                cache.appendleft(city)

    return answer
