#reverse a string iteratively and recursively

def get_reversed_iterative(item):

    reversed_string = ''
    for char in item:
        reversed_string = char + reversed_string
    return reversed_string


def get_reversed_recursive(item):

    if(len(item) == 0):
        return ""

    print(item[(len(item)-1)], end="")

    return get_reversed_recursive(item[:len(item)-1])


get_reversed_recursive('yoyo mastery')
