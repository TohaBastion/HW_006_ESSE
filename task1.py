"""task1"""


iterable = [1, "2", 15, "True", 'x + y = 20', "Київ", 7, 8, 9]

elements = iter(iterable)


while True:
    try:
        element = next(elements)
        print(element)
    except StopIteration:
        break
