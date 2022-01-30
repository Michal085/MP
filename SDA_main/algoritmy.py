for n in range(1000, 10001, 1000):
    pole = [random.randrange(n) for i in range(n)]
    tim = time.time()
    pocet = 0
    for i in range(n):
        for j in range(i + 1, n):
            if pole[i] == pole[j]:
                pocet += 1
    tim = time.time() - tim
    print(n, round(tim, 3))

element = 18
array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]

print("Searching for {}".format(element))
print("Index of {}: {}".format(element, binary_search_recursive(array, element, 0, len(array))))


