rows = int(input("Please enter the amount of rows you wish to be displayed: "))
number = 1

for i in range(1, rows + 1):
    for j in range(1, 1+i):
        print(number, end= " ")
        number= number + 1
    print()