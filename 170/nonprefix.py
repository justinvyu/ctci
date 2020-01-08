
def nonPrefixCode(s, d):
    p = {
        "": 1,
        "0": 1 if "0" in d.values() else 0,
        "1": 1 if "1" in d.values() else 0,
    }
    for v in d.values():
        p[v] = sum([
            p[v[len(t):]] for t in d.values() if t == v[:len(t)]
        ])
    for i in range(1, len(s) + 1):
        x = s[:i]
        p[x] = sum([
            p[x[len(t):]] for t in d.values() if t == x[:len(t)]
        ])
    return p[s]

if __name__ == "__main__":
    s = "10101"
    d = {
        "A": "1",
        "B": "01",
        "C": "101"
    }
    print(nonPrefixCode(s, d))
