import itertools
def solution(mylist):
    answer = []
    mylist.sort()
    answer+=(list(itertools.permutations(mylist,len(mylist))))
    return answer