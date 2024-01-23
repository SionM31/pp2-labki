# Create a generator that generates the squares of numbers up to some number N.

class MyNumbers:
    def __init__(self, N):
        self.N = N
    
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= self.N:
          x = self.num * self.num
          self.num += 1
          return x
        else:
          raise StopIteration


classik = MyNumbers(10)
iteratik = iter(classik)

for i in iteratik:
   print(i)