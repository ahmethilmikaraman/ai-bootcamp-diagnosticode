import random

def ort():
    for i in range(1_000_000):
        yield random.randint(0,200)

result = 0
for i in ort():
    result += i

print(result / 1_000_000)
    