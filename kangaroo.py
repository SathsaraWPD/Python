def start_details(x1, v1, x2, v2):
    if 0 <= x1 <= 10000 and 0 <= x2 <= 10000 and 1 <= v1 <= 10000 and 1 <= v2 <= 10000:
        kangaroo_1 = []
        kangaroo_2 = []

        for kan1 in range(x1, 10000, v1):
            kangaroo_1.append(kan1)
        
        for kan2 in range(x2, 10000, v2):
            kangaroo_2.append(kan2)
        
        for x, y in zip(kangaroo_1, kangaroo_2):
            if x == y:
                sum = 1
        if sum == 1:
            return "YES"
        else:
            return "NO"

    else:
        return False


x = int(input())
v = int(input())
y = int(input())
w = int(input())

start_details(x, v, y, w)





