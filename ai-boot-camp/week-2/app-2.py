
numbers = [1, 2, 3, 4, 5, 6]

print(list(map(lambda n: n**2 , numbers)))

#################################################

numbers = list(range(0,51))

print(list(filter(lambda n: n % 2 == 0,numbers)))

#################################################

summary = lambda n1, n2: sum(range(n1, n2 + 1)) 

result = summary(1,10)
print(result)

#################################################


