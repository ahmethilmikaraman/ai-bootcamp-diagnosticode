class EvenNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

        if not (self.start % 2 == 0):
            self.start += 1

        if not (self.stop % 2 == 0):
            self.stop += 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 2
            return x
        else:
            raise StopIteration
        
evens = EvenNumbers(12,30)

for i in evens:
    print(i)

print("########################")
evens = EvenNumbers(11,27)

for i in evens:
    print(i)


###############################################################

print("########################")

def fibonacci():
    a, b = 1, 1
    for i in range(10):
        yield a
        a, b = b, a + b

for i in fibonacci():
    print(i)