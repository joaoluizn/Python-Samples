""" 
    Python Generator Samples 
    
    Python Generators are a simple way to creating iterators. A Generator is a function that returns an iterator object
    which can be iterated one value at a time, where there is no need to implement __iter__ and __next__ functions, 
    since its automatically implemented. 

"""


def customGenerator(value):
    """ A simple generator function """
    for value in value:
        yield value

def anotherGenerator(value=0):
    """ Another simple generator function """
    value += 1
    yield value

    value+=2
    yield value

    value += -3
    yield value

if __name__ == "__main__":

    # This is a generator
    generator_from_function = customGenerator([1,2,3,4,5])

    # Another generator
    another_generator_from_function = anotherGenerator()

    # This is also a generator too
    generator_from_expression = (x for x in [1,2,3,4,5])

    print(f'Starting Generator iteration from Generator function:')
    for index in generator_from_function:
        print(index)

    print(f'\nStarting Generator iteration from another Generator function:')
    for k in another_generator_from_function:
        print(f'Current Value {k}')

    print(f'\nStarting Generator iteration from Generator Expression:')
    for index in generator_from_expression:
        print(index)

    print(f'\ngenerator_from_function: {type(generator_from_function)} == generator_from_expression: {type(generator_from_expression)}')