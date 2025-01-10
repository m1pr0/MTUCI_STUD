def max_of_two(num1, num2):
    return max(num1, num2)

def sqrt_num(num):
    return num ** 0.5

def num_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial