#comparing two functions to find the factorial of a number. One is recursive , the other should use a for loop.

def get_recursive_factorial(a):
    
    if(a == 2):
       return 2
    return a * get_recursive_factorial(a-1)
        
    

def get_iterative_factorial(n):
    max = n
    fact = 1
    for i in range(1, max+1):
        fact = fact * i
        
    return fact

print("Using recursion")
print(get_recursive_factorial(23))
print("Using iteration")
print(get_iterative_factorial(23))
