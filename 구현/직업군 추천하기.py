def solution(table, languages, preference):
    answer = ''
    result = []
    for comp in table:
        companyname,five,four,three,two,one = map(str,comp.split())
        score = 0
        for language,pref in zip(languages,preference):
            if five == language:
                score+=5*pref
            elif four == language:
                score+=4*pref
            elif three == language:
                score += 3 * pref
            elif two == language:
                score+=2*pref
            elif one == language:
                score+=pref
        result.append((score,companyname))
    result.sort(key = lambda l:(-l[0],l[1]))
    answer = result[0][1]
    return answer