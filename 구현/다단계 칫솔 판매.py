import math

Parent = {}
profit_table = {}

def go(child,profit):
    if child == '-':
        profit_table[child] += math.floor(profit)
        return
    parent = Parent[child]
    if profit < 10:
        profit_table[child] += profit
        return
    else:
        parent_profit = int(profit*0.1)
        profit_table[child] += profit - parent_profit
        go(parent,parent_profit)

def solution(enroll, referral, seller, amount):
    answer = []
    profit_table['-'] = 0
    for child,parent in zip(enroll,referral):
        Parent[child] = parent
        profit_table[child] = 0

    for who,n in zip(seller,amount):
        profit = 100*n
        go(who,profit)

    for who in enroll:
        answer.append(profit_table[who])
    return answer