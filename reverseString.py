#reverse a string iteratively and recursively

def get_reversed_iterative(item):

    reversed_string = ''
    for char in item:
        reversed_string = char + reversed_string
    return reversed_string


def get_reversed_recursive(item):

    


print(get_reversed_iterative('yoyo mastery'))
