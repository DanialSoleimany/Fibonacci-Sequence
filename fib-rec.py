def fib_rec(n):
    if (n <= 2):
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

n = int(input("n: "))

for i in range(1, n+1):
    print(fib_rec(i))