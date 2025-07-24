n= int(input("Enter the amount of rows you wish to be displayed: "))

for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print()