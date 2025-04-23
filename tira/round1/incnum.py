
def count_numbers(length, numbers):
    if "0" in numbers:
        add = 1 if length == 1 else 0
    else:
        add = 0   
    
    n=len(numbers)
    arr = sorted([int(c) for c in numbers if c!="0"])
    limit = length
    
    def rec(available, depth):
        if depth == limit:
            return 1
        res = 0
        for i in range(len(available)):
            res += rec(available[i:], depth+1)
        return res
    
    return rec(arr, 0) + add


        
        


if __name__ == "__main__":
    print(count_numbers(3, "123")) # 10
    print(count_numbers(5, "1")) # 1
    print(count_numbers(2, "137")) # 6
    print(count_numbers(8, "25689")) # 495
    print(count_numbers(1, "0")) # 1
    print(count_numbers(2, "0")) # 0
    print(count_numbers(10, "12")) # 11
    print(count_numbers(10, "123456789")) # 43758