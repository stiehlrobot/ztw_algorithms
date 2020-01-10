#create iterative and recursive solutions for fibonacci
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34


def get_iterative_fibonacci(n):

    first = 1
    last = 1
    newVal = 0
    for i in range(2,n):
        newVal = first + last
        if(i%2 == 0):
            first = newVal
        else:
            last = newVal

    return newVal



def get_recursive_fibonacci(n):

    #do code here
    if(n < 2):
        return n
    return get_recursive_fibonacci(n-1) + get_recursive_fibonacci(n-2)

print(get_iterative_fibonacci(12))
print(get_recursive_fibonacci(12))


