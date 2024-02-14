#factorial func

def factorial(n):
    fact = 1
    if n < 0:
        raise ValueError("Please, input integer >= 0")
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            fact = fact * i
        print(fact)
