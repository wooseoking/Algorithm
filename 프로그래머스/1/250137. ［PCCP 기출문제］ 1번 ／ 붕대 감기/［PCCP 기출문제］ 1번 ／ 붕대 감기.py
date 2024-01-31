def solution(bandage, health, attacks):
    answer = 0
    
    t,x,y = bandage
    
    T = attacks[-1][0]
    attacked = [False]*(T + 1)
    attackedTable = dict()
    
    for attackedTime, damage in attacks:
        attacked[attackedTime] = True
        attackedTable[attackedTime] = damage
        
    conTime = 0
    
    hp = health
    
    
    for time in range(0,T + 1):
        
        if attacked[time]:
            damage = attackedTable[time]
            hp-=damage
            if hp<=0:
                return -1
            conTime = 0
        else:
            hp+=x
            if conTime == t:
                hp += y
                conTime = 0
            if hp>=health:
                hp = health
        conTime += 1
    
    return hp