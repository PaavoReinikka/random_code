
def bin_packing(weights, max_weight):
    def backtrack(weights, bins):
        if not weights:
            return len(bins)
        
        min_bins = float('inf')
        for i in range(len(bins)):
            if sum(bins[i]) + weights[0] <= max_weight:
                bins[i].append(weights[0])
                min_bins = min(min_bins, backtrack(weights[1:], bins))
                bins[i].pop()
        
        bins.append([weights[0]])
        min_bins = min(min_bins, backtrack(weights[1:], bins))
        bins.pop()
        
        return min_bins
    
    weights.sort(reverse=True)
    return backtrack(weights, [])

def fill_box(weights, goal_weight):
    if goal_weight==0: return
    if goal_weight in weights:
        weights.remove(goal_weight)
        return
    for elem in weights:
        if elem<=goal_weight:
            weights.remove(elem)
            fill_box(weights, goal_weight-elem)
            break

def _min_count(weights, max_weight):
    acc=0
    n=len(weights)
    weights = sorted(weights)[::-1]
    while len(weights)>0:
        fill_box(weights, max_weight)
        acc+=1
        if acc>n: return -1
    return acc

def min_count(weights, max_weight):
    if not weights: return 0
    if max(weights)>max_weight: return -1
    if sum(weights)<=max_weight: return 1
    return bin_packing(weights, max_weight)


if __name__ == "__main__":
    print(min_count([2, 3, 3, 5], 7)) # 2
    print(min_count([2, 3, 3, 5], 6)) # 3
    print(min_count([2, 3, 3, 5], 5)) # 3
    print(min_count([2, 3, 3, 5], 4)) # -1

    print(min_count([], 1)) # 0
    print(min_count([1], 1)) # 1
    print(min_count([1, 1, 1, 1], 1)) # 4
    print(min_count([1, 1, 1, 1], 4)) # 1

    print(min_count([3, 4, 1, 2, 3, 3, 5, 9], 10)) # 3