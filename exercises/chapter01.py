
# 1.1 Is Unique

def is_unique(s):
    """
    Returns true if every character in the string s is unique.
    >>> is_unique("abcdefg")
    True
    >>> is_unique("aabbccdd")
    False
    """
    return len(set(s)) == len(s)

def is_unique_alt(s):
    """
    Returns true if every character in the string s is unique.
    >>> is_unique("abcdefg")
    True
    >>> is_unique("aabbccdd")
    False
    """
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                return False
    return True

# 1.2 Check Permutation

def check_permutation(a, b):
    """
    Returns true if one string is a permutation of the other.
    >>> check_permutation("abcd", "dcba")
    True
    >>> check_permutation("aaaa", "bbbb")
    False
    """
    if len(a) != len(b):
        return False
    chars_a, chars_b = {}, {}
    for c1, c2 in zip(list(a), list(b)):
        chars_a[c1] = chars_a.get(c1, 0) + 1
        chars_b[c2] = chars_b.get(c2, 0) + 1
    for key in chars_a:
        if chars_b.get(key, 0) != chars_a[key]:
            return False
    return True

# 1.3 URLify

def urlify(s, n):
    """
    Returns a URLified version of s using the first n characters.
    >>> urlify("Mr John Smith    ", 13)
    'Mr%20John%20Smith'
    """
    s = s[:n]
    return s.replace(" ", "%20")
