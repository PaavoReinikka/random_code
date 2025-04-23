import itertools

def check_sum(numbers):
    s = sum(numbers)
    if s % 2 == 1:
        return False
    s //= 2
    if s in numbers:
        return True
    coefs = itertools.product([0, 1], repeat=len(numbers))
    foo = lambda x: sum(a*b for a, b in zip(x, numbers))
    for coef in coefs:
        if foo(coef) == s:
            return True
    return False



if __name__ == "__main__":
    print(check_sum([1, 2, 3, 4])) # True
    print(check_sum([1, 2, 3, 5])) # False
    print(check_sum([0])) # True
    print(check_sum([2, 2])) # True
    print(check_sum([2, 4])) # False
    print(check_sum([1, 5, 6, 3, 5])) # True
    print(check_sum([1, 5, 5, 3, 5])) # False
    print(check_sum([10**9, 2*10**9, 10**9])) # True
    print(check_sum([1, 1, 1, 1, 1, 1, 1, 1, 1, 123])) # False