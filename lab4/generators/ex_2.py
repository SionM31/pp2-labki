# Write a program using generator to print the even numbers between 0
# and n in comma separated form where n is input from console.

class MyNumbers:
    def __init__(self, num):
        self.n = num

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
         if self.num <= self.n:
            x = self.num
            self.num += 2
            return ", " * bool(x) + str(x)
         else:
            raise StopIteration


num = int(input())
classik = MyNumbers(num)
iteratik = iter(classik)

for i in iteratik:
    print(i, end="")
