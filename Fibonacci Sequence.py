n = int(input("Number of sentences: "))
x = 0
y = 1
print(y, end = " ")
for i in range(1, n):
    z = x + y
    print(z, end = " ")
    x = y
    y = z
