import functools
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am created by a function \
    passed as an argument.")
    print(greeting)

greet(shout)
greet(whisper)


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

print(functools.reduce(lambda x,y: x+y, [47,11,42,13]))

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]

even_fibonacci_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_fibonacci_numbers)