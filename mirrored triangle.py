n= int(input("Enter the amount of rows you wish to be displayed: "))

for i in range(1, n+1):
    for x in range(n-i):
        print(" ", end = " ")
    for j in range(i):
        print("* ", end="")
    print()