
def all_even_generator():
    n = 0
    while True:
        yield n
        n += 2

c = 0
for item in all_even_generator():
    print("Generated Item " + str(item))
    if c == 3: break
    c += 1