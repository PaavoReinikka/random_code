import itertools

def count_combinations(cards, target):
    acc = 0
    foo = lambda x: sum([c*val for c, val in zip(x, cards)]) == target
    for coefs in list(itertools.product([0, 1], repeat=len(cards))):
        acc += foo(coefs)
    return acc
    

if __name__ == "__main__":
    print(count_combinations([2, 1, 4, 6], 6)) # 2
    print(count_combinations([1, 1, 1, 1], 2)) # 6
    print(count_combinations([2, 1, 4, 6], 15)) # 0
    print(count_combinations([1], 1)) # 1
    print(count_combinations([1, 2, 3, 4, 5], 5)) # 3
    print(count_combinations([1, 1, 4, 1, 1], 4)) # 2
    print(count_combinations([1] * 10, 5)) # 252
