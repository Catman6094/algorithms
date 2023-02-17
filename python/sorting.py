# INSERTION SORT

class _inf:
    def __gt__(self, other):
        return True
    
    def __lt__(self, other):
        return False


def insertion_sort(A):
    for i in range(1, len(A)):
        v = A[i]
        j = i - 1
        while A[j] > v and j >= 0:
            A[j + 1] = A[j]
            j = j-1
        A[j + 1] = v


# MERGE SORT
def merge(A, left, mid, right):
    # Merge A[left:mid] and A[mid:right]
    
    # Create arrays with infinite sentinel values
    L = A[left:mid]
    R = A[mid:right]
    L.append(_inf())
    R.append(_inf())
    
    li = 0
    ri = 0
        
    for i in range(left, right):
        if L[li] > R[ri]:
            A[i] = R[ri]
            ri += 1
        else:
            A[i] = L[li]
            li += 1

    
 
def merge_sort(A, left, right):
    # Sorts in [left:right]
    if right - left > 1:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


if __name__ == "__main__":
    ns = [3, 2, 6, 5, 1, 4]
    insertion_sort(ns)
    assert ns == [1, 2, 3, 4, 5, 6]
    
    ns = [3, 2, 6, 5, 1, 4]
    merge_sort(ns, 0, len(ns))
    assert ns == [1, 2, 3, 4, 5, 6]