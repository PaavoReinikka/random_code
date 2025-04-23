import time

def can_create(coins, target):
    def rec(coins, target, memo):
        if target < 1:
            return target == 0
        if target in memo:
            return memo[target]
        
        for coin in coins:
            if rec(coins, target - coin, memo):
                return True
            
        memo[target] = False
        return False
    
    #memo = {i: True for i in coins + [0]}
    #return rec(coins, target, memo)
    return rec(coins, target, {})


def _can_create(coins, target):
    memo = set(coins +  [0])
    
    for i in range(1, target + 1):
        for coin in coins:
            if i - coin in memo:
                memo.add(i)
    
    return target in memo


  
            

if __name__ == "__main__":
    print(can_create([1, 2, 5], 13)) # True
    print(can_create([2, 4, 6], 13)) # False
    print(can_create([1], 42)) # True
    print(can_create([2, 4, 6], 42)) # True
    print(can_create([3], 1337)) # False
    print(can_create([3, 4], 1337)) # True

    start = time.time()
    print(can_create([11, 22, 33], 331))
    print(time.time() - start) 