n = int(input())
query = []
for _ in range(n):
    query.append(input())
res = []
for word in query:
    if word[-1] == 'a':
        temp = word
        temp +="s"
        res.append(temp)
    elif word[-1] == 'i' or word[-1] == 'y':
        temp = word[:len(word)-1]
        temp+="ios"
        res.append(temp)
    elif word[-1] == 'l':
        temp = word[:len(word)-1]
        temp += "les"
        res.append(temp)
    elif word[-1] == 'n' or word[len(word)-2:] == "ne":
        if word[-1]=='n':
            temp = word[:len(word)-1]
            temp +="anes"
            res.append(temp)
        elif word[len(word)-2:] == "ne":
            temp = word[:len(word)-2]
            temp+="anes"
            res.append(temp)
    elif word[-1] == 'o':
        temp = word
        temp+="s"
        res.append(temp)
    elif word[-1] == 'r':
        temp = word
        temp += "es"
        res.append(temp)
    elif word[-1] == 't':
        temp = word
        temp += "as"
        res.append(temp)
    elif word[-1] == 'u':
        temp = word
        temp += "s"
        res.append(temp)
    elif word[-1] == 'v':
        temp = word
        temp += "es"
        res.append(temp)
    elif word[-1] == 'w':
        temp = word
        temp += "as"
        res.append(temp)
    else:
        temp = word
        temp+="us"
        res.append(temp)
for word in res:
    print(word)