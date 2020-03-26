def add(x):
    def inner(y):
        return x + y
    return inner

add_plus3 = add(3)


print("Closure " + str(add_plus3(2)))
