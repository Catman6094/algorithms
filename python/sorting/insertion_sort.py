def insertion_sort(ns):
    for i in range(1, len(ns)):
        v = ns[i]
        j = i - 1
        while ns[j] > v and j >= 0:
            ns[j + 1] = ns[j]
            j = j-1
        ns[j + 1] = v
        
        

ns = [3, 2, 6, 5, 1, 4]

insertion_sort(ns)
print(ns)