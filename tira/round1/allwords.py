from collections import OrderedDict

def rec(prev, inds, chars):

    if len(inds)==len(chars): yield prev
    else:
        for i, char in enumerate(chars):
            if i in inds:
                continue
            elif prev and prev[-1]==char:
                continue
            else:
                yield from rec(prev + char, inds + [i], chars)


def create_words(word):
    chars = sorted([c for c in word])
    n = len(chars)
    result = OrderedDict()
    for w in rec("", [], chars):
        result[w] = None
    return list(result.keys())


if __name__ == "__main__":

    # test that all lists are sorted
    assert all([sorted(create_words(w)) == create_words(w) for w in ["abc", "aab", "aaab", "kala", "syksy", "aybabtu", "abcdefgh"]])

    print(create_words("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create_words("aab")) # ['aba']
    print(create_words("aaab")) # []

    print(create_words("kala"))
    # ['akal', 'akla', 'alak', 'alka', 'kala', 'laka']

    print(create_words("syksy"))
    # ['ksysy', 'kysys', 'skysy', 'syksy', 'sykys', 'sysky', 
    #  'sysyk', 'yksys', 'ysksy', 'yskys', 'ysyks', 'ysysk']

    print(len(create_words("aybabtu"))) # 660
    print(len(create_words("abcdefgh"))) # 40320


