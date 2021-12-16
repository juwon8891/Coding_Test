def fizzBuzz(o):
    for n in range(1,o+1):
        if (n % 3 == 0) & (n % 5 != 0):
            print("Fizz")
        elif (n % 5 == 0) & (n % 3 != 0):
            print("Buzz")
        elif (n % 3 == 0) & (n % 5 == 0):
            print("FizzBuzz")
        else:
            print(n)