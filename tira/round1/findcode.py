import re
import itertools
import time
import random

class Oracle:
    def __init__(self, code):
        self.code = code
        self.counter = 0

    def check_code(self, code):
        self.counter += 1
        if self.counter > 16:
            raise RuntimeError("too many check_code calls")

        if type(code) != str or not re.match("^[1-9]{4}$", code) or len(code) != len(set(code)):
            raise RuntimeError("invalid code for check_code")

        in_place = in_code = 0
        for pos in range(4):
            if code[pos] in self.code:
                if code[pos] == self.code[pos]:
                    in_place += 1
                else:
                    in_code += 1

        return in_place, in_code

def find_code(oracle):
    
    guess = "1234"
    codes = [''.join(p) for p in itertools.permutations('123456789', 4) if p!=('1','2','3','4')]

    for count in range(16):
        in_place, in_code = oracle.check_code(guess)
        if in_place == 4:
            #print("Oracle called", count, "times")
            return guess, count
        
        pruned_codes = []
        for code in codes:
            #n_inplace = sum(a==b for a, b in zip(code, guess))
            n_inplace = len([1 for i in range(4) if code[i] == guess[i]]) # faster
            #n_incode = len(set(code) & set(guess)) - n_inplace
            n_incode = len([1 for i in range(4) if code[i] in guess]) - n_inplace # faster
            if n_inplace == in_place and n_incode == in_code:
                pruned_codes.append(code)
        
        guess = pruned_codes[0]
        codes = pruned_codes[1:]
        
    #print("Oracle called 16 times but no solution found")
    return None, 16

if __name__ == "__main__":
    # esimerkki oraakkelin toiminnasta
    oracle = Oracle("4217")
    print(oracle.check_code("1234")) # (1, 2)
    print(oracle.check_code("3965")) # (0, 0)
    print(oracle.check_code("4271")) # (2, 2)
    print(oracle.check_code("4217")) # (4, 0)

    # esimerkki funktion find_code toiminnasta
    oracle = Oracle("4217")
    code = find_code(oracle)
    print(code) # 4217
    
    
    test_codes = [''.join(p) for p in itertools.permutations('123456789', 4) if p!=('1','2','3','4')]
    print("Number of possible codes:", len(test_codes))
    #n_tests = 100
    n_tests = len(test_codes)
    #test_codes = random.sample(test_codes, n_tests)
    acc = 0
    mx, mn = 0, 16
    start = time.time()
    for code in test_codes:
        oracle = Oracle(code)
        guess,count = find_code(oracle)
        assert code == guess
        if guess == code:
            acc += count
            mx = max(mx, count)
            mn = min(mn, count)
    print("Time:", time.time()-start)
    print("All tests passed")
    print("Average oracle calls:", acc/n_tests)
    print("Max oracle calls:", mx)
    print("Min oracle calls:", mn)
    