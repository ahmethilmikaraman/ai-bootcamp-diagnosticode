from functools import reduce

numbers = [1, 2, 3, 4, 5]

def edit_lists(edit):
    def square(liste):
        return list(map(lambda n: n*n, liste))

    def find_evens(liste):
        return list(filter(lambda n : n % 2 == 0, liste))
    
    def multiply(liste):
        return reduce(lambda x, y: x*y, liste)

    if edit == "square":
        return square
    if edit == "find_evens":
        return find_evens
    if edit == "multiply":
        return multiply

square = edit_lists("square")
print(square(numbers))

find_evens = edit_lists("find_evens")
print(find_evens(numbers))

multiply = edit_lists("multiply")
print(multiply(numbers))


##################################################################

people = [
  {"name": "Ahmet", "age": 25},
  {"name": "Ayşe", "age": 30},
  {"name": "Mehmet", "age": 20}
]

sorted_byage = sorted(people, key = lambda person: person["age"])
print(sorted_byage)