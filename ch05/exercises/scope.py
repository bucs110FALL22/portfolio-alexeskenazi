def multiply(a, b):
    total = 0
    for i in range(a):
        total = total + b
    return total

    
def exponent(exp, base):
    total = 1
    for i in range(exp):
        total = total * base
    return total


def square(a):
    return exponent(2,a)


print('5x6 = ' + str(multiply(5, 6)))
print('6^5 = ' + str(exponent(5, 6)))
print('6^2 = ' + str(square(6)))
