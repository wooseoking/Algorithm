query = ''
while True:
    try:
        query += input()
    except EOFError:break
query = sum(map(int,query.split(',')))
print(query)