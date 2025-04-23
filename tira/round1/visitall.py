def make_adjacency_map(M):
    n = len(M)
    adj = {i: [] for i in range(1,n+1)}
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i+1].append((j+1, M[i][j]))
    return adj


def find_route(distances):
    adj = make_adjacency_map(distances)
    n = len(adj)
    
    def rec(visited, acc=0, best=float('inf')):
        if acc>=best:
            return (float('inf'), None)
        current = visited[-1]
        if len(visited)==n:
            return acc + distances[current-1][0], visited + [1]
        
        best = (float('inf'), None)
        for node, weight in adj[current]:
            if node not in visited:
                best = min(best, rec(visited + [node], acc + weight, best[0]))
                
        return best

    return rec([1])


if __name__ == "__main__":
    distances = [[0, 2, 2, 1, 8],
                 [2, 0, 9, 1, 2],
                 [2, 9, 0, 8, 3],
                 [1, 1, 8, 0, 3],
                 [8, 2, 3, 3, 0]]

    length, route = find_route(distances)
    print(length) # 9
    print(route) # [1, 3, 5, 2, 4, 1]

    distances = [[0, 7, 5, 9, 6, 3, 1, 3],
                 [7, 0, 3, 2, 3, 3, 7, 8],
                 [5, 3, 0, 4, 2, 7, 7, 1],
                 [9, 2, 4, 0, 2, 3, 2, 4],
                 [6, 3, 2, 2, 0, 9, 5, 9],
                 [3, 3, 7, 3, 9, 0, 4, 5],
                 [1, 7, 7, 2, 5, 4, 0, 7],
                 [3, 8, 1, 4, 9, 5, 7, 0]]

    length, route = find_route(distances)
    print(length) # 18
    print(route) # [1, 7, 4, 6, 2, 5, 3, 8, 1]