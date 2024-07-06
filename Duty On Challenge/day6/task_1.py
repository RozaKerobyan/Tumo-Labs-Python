n = int(input("Enter a number between 1 and 20: "))
if 1 <= n <= 20:
    for i in range(n):
        i *= i
        print(i)
