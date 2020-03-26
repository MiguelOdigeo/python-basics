def get_even_comprehension(n):
    def is_even(x):
        return x % 2 == 0
    return [x for x in range(n+1) if is_even(x)]


print("First even numbers until 10: " + str(get_even_comprehension(10)))