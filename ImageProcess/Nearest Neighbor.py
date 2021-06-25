print("Refr, Refc")
refr,refc = map(int,input().split())
print("change_r, change_c")
row,col = map(int,input().split())
print("ROWS Transformed")
for i in range(row):
    print(int((refr/row)*i + 0.5),end=' ')
print()
print("COLS Transformed")
for j in range(col):
    print(int((refc / col) * j + 0.5  ), end=' ')