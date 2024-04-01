"""task3"""


class ReverseIterator:
    """Клас повертаючий елементи списку в зворотньому порядку."""
    def __init__(self, iterable):
        self._iterable = iterable
        self._index = len(iterable) - 1


    def __iter__(self):
        return self


    def __next__(self):
        if self._index >= 0:
            value = self._iterable[self._index]
            self._index -= 1
            return value
        else:
            raise StopIteration('У списку немає значень!')


my_list = [1, "2", 15, "True", 'x + y = 20', "Київ", 7, 8, 9]
reverse_iter = ReverseIterator(my_list)

for item in reverse_iter:
    print(item)
