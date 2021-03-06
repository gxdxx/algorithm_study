def result(k, n):
    if(k == 0):
        return n
    if(n == 1):
        return 1

    if (apartment[k][n] != 0):
        return apartment[k][n]

    apartment[k][n] = result(k-1, n) + result(k, n-1)
    return apartment[k][n]

T = int(input())

apartment = [[0]*15 for _ in range(15)]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(result(k,n))