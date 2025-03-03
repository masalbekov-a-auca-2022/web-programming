square = lambda x : x*x

print(square(5))

sum_all = lambda *args: sum(args)

print(sum_all(1,2,3,4))

def fib(n):
    if n <=1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))

def prime(num, divisor=None):
    if divisor is None:
        divisor = num - 1
    if num <= 1:
        return False
    if divisor == 1:
        return True
    if num % divisor == 0:
        return False
    return prime(num, divisor - 1)

print(prime(5))
print(prime(4))