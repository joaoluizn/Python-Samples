""" 

Understanding Equality vs Identity Common Scenarios

There are two common comparisons in Python, the '==' and 'is' operators

But what is the real difference between them?
Alright, to get things star'a'ted its important to understand
that '==' means for equality and 'is' for identity.

So lets check this on code!

"""


def main():
    """
    To better illustrate the difference we can check lets see how things works with lists and dicts
    """
    print("Using Lists:")
    a = ['rabbit', 'owl', 'frog']
    b = a

    print("When b = a:")
    print("a == b? ", a == b)  # True
    print("a is b?", a is b)  # True

    b = list(a)

    print("\nWhen b = list(a):")
    print("a == b?", a == b)  # True
    print("b is a?", a is b)  # False

    print("\nUsing Dicts")
    dc1 = dict(first=10, second=30)
    dc2 = dc1

    print("When dc2 = dc1:")
    print("dc1 is dc2?", dc1 is dc2)
    print("dc1 == dc2?", dc1 == dc2)

    dc2 = dict(dc1)
    print("\nWhen dc2 = dict(dc1):")
    print("dc1 is dc2?", dc1 is dc2)
    print("dc1 == dc2?", dc1 == dc2)

    """ 
    Two things are happening here:
        First case:
            - when we do a = b, we are saying a is pointing to b, so a is like b.
            - But their content are still equally comparable with a == b.
        Second case:
            - when we do a = dict/list/set/(b) we are creating a new object with a new memory id
            - But their content are still equally comparable with a == dict/list/set(b)
            - NODE: this doesn't work with tuple and str
    
    The reason for this is that when we explicitly create a new object, the original reference from the 
    object is lost, so it's important to know this concept because sometimes you could unintentionally change an object 
    that shouldn't be changed when trying to or create a temporary like 'aux = object'. As previously stated, 
    some objects don't behave like that, like str() and tuple().
    
    For more about how to avoid mistakes like this, check the documentation about shallow and deep copy.
    - https://docs.python.org/3.7/library/copy.html
    
    Thanks for reading and feel free to contribute or leave some feedback.

    """


if __name__ == '__main__':
    main()
