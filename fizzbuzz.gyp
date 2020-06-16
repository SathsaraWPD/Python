def fizzbuzz ( num ):
    if num > 0 and num < 200000:
        for i in range (1, num + 1):
            if (i % 3) == 0 and (i % 5) == 0:
                print("fizzbuzz")
            elif (i % 3) == 0 and (i % 5) != 0:
                print("fizz")
            elif (i % 3) != 0 and (i % 5) == 0:
                print("buzz")
            else:
                print(i)
    else:
        print("invalid")

n = int(input("Enter the  number if you want : "))

fizzbuzz(n)
