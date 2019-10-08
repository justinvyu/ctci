from queue import Queue

def quicksort(x):
    """
    Quicksort algorithm: pick a random pivot p (first elem), put all
    elements < p in one list, all elements >= p in another, then make
    recursive call on each, and combine the two lists
    Base case: empty list or list of size 1
    >>> x = [3, 2, 4, 6, 7, 2, 1, 3]
    >>> quicksort(x) == sorted(x)
    True
    >>> x = [1]
    >>> quicksort(x) == sorted(x)
    True
    """
    def quicksort_helper(lst):
        if len(lst) <= 1:
            return lst
        p = lst[0]
        left = [item for item in lst if item < p]
        middle = [item for item in lst if item == p]
        right = [item for item in lst if item > p]
        return quicksort_helper(left) + middle + quicksort_helper(right)
    return quicksort_helper(x)

def merge(a, b):
    """
    Performs a merge operation on two sorted lists
    >>> a = [1, 4, 5, 8, 10, 12]
    >>> b = [2, 4, 6, 7]
    >>> merge(a, b) == sorted(a + b)
    True
    >>> a = [1, 2, 3]
    >>> b = []
    >>> merge(a, b) == a
    True
    """
    i, j = 0, 0
    output = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            output.append(a[i])
            i += 1
        elif a[i] > b[j]:
            output.append(b[j])
            j += 1
    if i < len(a):
        output += a[i:]
    elif j < len(b):
        output += b[j:]
    return output

def mergesort(x):
    """
    Recursive version
    Merge sort algorithm: split into 2 halves, recursively
    sort the subproblems, utilizing the `merge` subroutine
    to combine two sorted lists into one sorted list
    """
    if len(x) <= 1:
        return x
    mid = len(x) // 2
    left, right = mergesort(x[:mid]), mergesort(x[mid:])
    return merge(left, right) 
     
def mergesort_iter(x):
    queue = Queue() 
    pass

if __name__ == '__main__':
    x = [3, 2, 4, 6, 7, 2, 1, 3]
    sorted_x = sorted(x)
    print('BEFORE QUICKSORT')
    print(x, sorted_x)
    print('AFTER QUICKSORT')
    print(quicksort(x), sorted_x)

    print('BEFORE MERGESORT')
    print(x, sorted_x)
    print('AFTER MERGESORT')
    print(mergesort(x), sorted_x)
