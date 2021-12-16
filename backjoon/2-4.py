a = int(input())
b = int(input())
if (a > 0) & (b > 0):
    print(int("1"))
elif (a < 0) & (b > 0):
    print(int("2"))
elif (a < 0) & (b < 0):
    print(int("3"))
elif (a > 0) & (b < 0):
    print(int("4"))