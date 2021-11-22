rows = int(input("Enter number 0f rows:"))
for i in range(rows, 1, -1):
    for space in range(0, rows-i):
         print(" ", end="")
    for j in range(i, 1*i-1):
        print("", "* ", end="")
    for j in range(0, i - 1):
        print("", "* ", end="")
    print("\n")

