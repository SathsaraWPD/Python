def find_odd_even(num):
    if num >= 0 and num <= 100:
        if (num % 2) == 0 and num >= 2 and num <= 5:
            print("Not Weird")

        elif (num % 2) == 0 and num >= 6 and num <=20:
            print("Weird")

        elif (num % 2) == 0 and num >20:
            print("Not Weird")

        else:
            print("Weird")
    else:
        print("Not Weird")

a = int(input())
find_odd_even(a)
