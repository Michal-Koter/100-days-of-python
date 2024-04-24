def add(*args):
    sum = 0
    for num in args:
        sum += num

    return sum

print(add(1, 2, 3, 4, 5))

def calculate(n, **kwargs):
    # print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3, multiply=5)