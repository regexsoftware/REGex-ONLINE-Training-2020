rows = 8
# rows = int(input("enter the number of rows"))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        #multiplication current column and row
        square = i * j
        print("", i * j, end='')
    print()

