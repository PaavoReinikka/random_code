def get_candidates(pattern):
    used = [e for e in pattern if e != "?"]
    candidates = [e for e in "123456789" if e not in used]
    return pattern.index("?"), candidates
    

def fill_first_missing(pattern):
    new_patterns = []
    ind, candidates = get_candidates(pattern)
    for cand in candidates:
        new_pattern = pattern[:ind] + cand + pattern[ind+1:]
        new_patterns.append(new_pattern)
    return new_patterns


def find_codes(pattern):
    patterns = [pattern]
    for i in range(pattern.count("?")):
        new_patterns = []
        for pattern in patterns:
            new_patterns.extend(fill_first_missing(pattern))
        patterns = new_patterns
    return patterns


if __name__ == "__main__":
    codes = find_codes("24?5")
    print(codes) # ['2415', '2435', '2465', '2475', '2485', '2495']

    codes = find_codes("1?2?")
    print(codes[:5]) # ['1324', '1325', '1326', '1327', '1328']
    print(len(codes)) # 42

    codes = find_codes("????")
    print(codes[:5]) # ['1234', '1235', '1236', '1237', '1238']
    print(len(codes)) # 3024