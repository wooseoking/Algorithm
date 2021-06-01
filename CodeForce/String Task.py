query = input().lower().strip()
Vowels = { "a", "o", "y", "e", "u", "i"}
ans = ""
for val in query:
    if val not in Vowels:
        ans +="." + val
print(ans)