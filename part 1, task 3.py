n = int(input())
if n < 0:
    n1 = n
    n2 = int(str(n * -1) * 2)
    n22 = -n2
    n3 = int(str(n * -1) * 3)
    n33 = -n3
    print(n1 + n22 + n33)
else:
    n1 = str(n)
    n2 = n1 * 2
    n3 = n1 * 3
    print(int(n1) + int(n2) + int(n3))