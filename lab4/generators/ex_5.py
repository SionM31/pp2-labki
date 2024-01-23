# Implement a generator that returns all numbers from (n) down to 0.

def implementor(n):
    for i in range(n, -1, -1):
        yield i


n = int(input())
listik = implementor(n)
print(*listik)