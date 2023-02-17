# INSERTION SORT

def insertion_sort(A):
    for i in range(1, len(A)):
        v = A[i]
        j = i - 1
        while A[j] > v and j >= 0:
            A[j + 1] = A[j]
            j = j-1
        A[j + 1] = v


# MERGE SORT
def _merge(A, left, mid, right):
    # Merge operation for merge sort
    
    # Create arrays with infinite sentinel values
    L = A[left:mid+1]
    R = A[mid+1:right+1]
    
    li = 0
    ri = 0
    i = left
    while li < len(L) and ri < len(R):
        if L[li] < R[ri]:
            A[i] = L[li]
            li += 1
        else:
            A[i] = R[ri]
            ri += 1
        i += 1
    
    if li == len(L):
        while ri < len(R):
            A[i] = R[ri]
            ri += 1
            i += 1
    else:
        while li < len(L):
            A[i] = L[li]
            li += 1
            i += 1

    
 
def merge_sort(A, left=None, right=None):
    # Sorts in [left:right+1]
    
    if left is None: left = 0
    if right is None: right = len(A) - 1
    
    if right - left > 0:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid+1, right)
        _merge(A, left, mid, right)


if __name__ == "__main__":
    ns = [3, 2, 6, 5, 1, 4]
    insertion_sort(ns)
    assert ns == [1, 2, 3, 4, 5, 6]
    
    ns = [3, 2, 6, 5, 1, 4]
    merge_sort(ns)
    assert ns == [1, 2, 3, 4, 5, 6]
    
    ns = [3, 2, 6, 5, 1, 4]
    merge_sort(ns, 1, 4)
    assert ns == [3, 1, 2, 5, 6, 4]