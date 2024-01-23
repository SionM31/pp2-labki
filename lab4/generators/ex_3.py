# Define a function with a generator which can iterate the numbers,
# which are divisible by 3 and 4, between a given range 0 and n.

class MyNumbers:
    def __init__(self, num):
        self.n = num

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
         if self.num <= self.n:
            x = self.num
            self.num += 1
            if x % 4 == 0 or x % 3 == 0:
                return ", " * bool(x) + str(x)
            else:
                return ""
         else:
            raise StopIteration


num = int(input())
classik = MyNumbers(num)
iteratik = iter(classik)

for i in iteratik:
    print(i, end="")
