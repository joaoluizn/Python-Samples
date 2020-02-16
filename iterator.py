""" Python Iterator implementation samples """

class infiniteIterator:
    """ infinite iterator over a given iterable object """

    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

class finiteIterator:
    """ finite iterator over a given iterable object """

    def __init__(self, value):
        self.value = value
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.value):
            next_value = self.value[self.index]
            self.index += 1
            return next_value
        else:
            # the for structure in python waits for an StopIteration exception to be raised
            # So it can finally finish the iteration process.
            raise StopIteration


if __name__ == "__main__":
    # An infinite iterator to represent the core functionality
    iterator = infiniteIterator([1,2,3,4])

    # A finite iterator just to show how __next__ and __iter__ works
    finite_iterator = finiteIterator([1,2,3,4])
    
    for i in finite_iterator:
        print(i)
