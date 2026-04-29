def fibonacci(n):
    if n < 0:
        return None
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#test
for i in range(1, 11):
    print(i, "->", fibonacci(i))