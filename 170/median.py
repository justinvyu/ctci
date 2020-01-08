from typing import List

def findMedian(arr: List[int]) -> int:
    """
    Finds the median of an unsorted array `arr`
    Runtime: average case of O(n)
    >>> arr = [1, 2, 3, 4, 5]
    >>> findMedian(arr)
    3
    >>> arr = [3, 1, 2, 4, 5]
    >>> findMedian(arr)
    3
    >>> arr = [3, 3, 2, 4, 5, 6, 6, 1, 2, 0]
    >>> findMedian(arr)
    3.0
    """
    def select(x: List[int], k: int) -> int:
        """
        Selects the kth smallest element of the array x
        """
        p = x[0]
        left, middle, right = [], [], []
        for a in x:
            if a < p:
                left.append(a)
            elif a == p:
                middle.append(a)
            else:
                right.append(a)

        if k < len(left):
            return select(left, k)
        elif k < len(left) + len(middle):
            return p
        else:
            return select(right, k - len(left) - len(right))

    if len(arr) % 2 == 1:
        return select(arr, len(arr) // 2)
    else:
        return (select(arr, len(arr) // 2) + select(arr, len(arr) // 2 + 1)) / 2 

def findMedianDeterministic(A):
    """
    Uses median of medians strategy to deterministically choose
    a pivot. Gives a tight O(n) bound.
    """
    pass

