def quicksort(a, l, r):
    if(r > l):
        v = a[r]
        i = l - 1
        j = r
        # partition
        while(True):
            i = i + 1
            j = j - 1
            while(a[i] < v):
                i = i + 1
            while(a[j] > v):
                j = j - 1
            if(i >= j):
                break
            t = a[i]
            a[i] = a[j]
            a[j] = t
        t = a[i]
        a[i] = a[r]
        a[r] = t
        # next sort
        quicksort(a, l, i - 1)
        quicksort(a, i + 1, r)

ary = [7, 8, 1, 2, 3, 4, 13, 5, 1, 2, 44, 5, 1]
quicksort(ary, 0, len(ary) - 1)
print ary


def quicksort2(array, indexL, indexR):
    if(indexR > indexL):
        i = 1  # partition(indexL, indexR)
        quicksort2(array, indexL, i - 1)
        quicksort2(array, i + 1, indexR)
