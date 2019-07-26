""" General Arguments Types Samples """


def hello_arguments(required_one, *args, **kwargs):
    return f"Required Arg: {required_one}\nPositional Args: {args}\nKey Args: {kwargs}\n"


""" 
Values are just samples to represent arguments. 
Focus on how apply different types of args.
Note: 
    Positional args are mapped to a tuple;
    Key Arguments are mapped to dictionary with key and values;
"""

if __name__ == "__main__":
    # Required argument, note positional and key args aren't obligatory
    print(hello_arguments(10))

    # Required and 2 positional args
    print(hello_arguments(10, 20, 30))

    # Required, positional and key arguments, possibilities starts to grow.
    print(hello_arguments(10, 20, 30, 40, id=20, value=30))

    # Required and Key Arguments.
    print(hello_arguments(10, id=20, value=30))
