a = 1
while a == 1:
    x = input("Enter a number to determine whether its even or odd: ")
    y = int(x)% 2
    if y == 1:
        print(x + " is an odd number")
    if y == 0:
        print(x + " is an even number")
