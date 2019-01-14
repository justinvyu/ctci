
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

# 1.4 Palindrome Permutation

def is_palindrome_permutation(s):
    """
    Returns true if a reordering of the characters in s can produce a palindrome. O(n)
    >>> is_palindrome_permutation("Tact Coa")
    True
    >>> is_palindrome_permutation("ab ab   ab ")
    False
    """
    s = s.replace(" ", "").lower()
    # Generate a dictionary, key (character) -> value (count)
    count = {}
    for i in range(len(s)):
        key = s[i]
        count[key] = count.get(key, 0) + 1
    odds = map(lambda x: x % 2, count.values())
    return sum(odds) == 1

# 1.5 One Away

def is_one_away(a, b):
    """
    Returns true if one of the strings a or b can be modified by inserting, removing
    or replacing a character to match the other string. Return true if the two strings
    are already identical (zero edits).
    >>> is_one_away("pale", "ple")
    True
    >>> is_one_away("pales", "pale")
    True
    >>> is_one_away("pale", "bale")
    True
    >>> is_one_away("pale", "bake")
    False
    >>> is_one_away("pale", "pale")
    True
    """
    if len(a) < len(b):
        a, b = b, a
    for i in range(len(a)):
        removed_a = a[:i] + a[i+1:]
        removed_b = b[:i] + b[i+1:]
        if removed_a == b or removed_a == removed_b:
            return True
    return False

# 1.6 String Compression

def string_compress(s):
    """
    Returns a 'compressed' version of the string that joins each letter as well as its
    consecutive frequency. Returns the original string if the 'compressed' version is
    longer.
    >>> string_compress("aabcccccaaa")
    'a2b1c5a3'
    >>> string_compress("abc")
    'abc'
    """
    compressed = ""
    current, count = "", 0
    for i in range(len(s)):
        if current and current != s[i]:
            compressed += current + str(count)
            current, count = s[i], 1
        else:
            current, count = s[i], count + 1
    compressed += current + str(count)
    return min(compressed, s, key=lambda x: len(x))
