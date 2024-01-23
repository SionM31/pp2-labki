# Implement a generator called squares to yield the square of all numbers from (a) to (b).
# Test it with a "for" loop and print each of the yielded values.

def square_yield(a, b):
    for i in range(a, b + 1):
        yield i * i


a, b = map(int, input().split())

listik = square_yield(a, b)
print(*listik)


for i in range(a, b + 1):
    print(i * i, end=" ")