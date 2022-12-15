# Write a Python function to find the nth term of Fibonacci sequence and its
# factorial. Return the result as a list
def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_fac(n):
    result = [fibonacci(n), factorial(n)]
    return result


if __name__ == "__main__":
    n = int(input("Enter a number : "))
    print(f"fibonacci and factorial : {fib_fac(n)}")
