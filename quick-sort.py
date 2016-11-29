import sys

def partition(a, s, e):
    p = s+1
    i = s+1
    while (i <= e):
        if (a[i] < a[s]):
            a[p], a[i] = a[i], a[p]
            p += 1
        i += 1
    a[s], a[p-1] = a[p-1], a[s]
    return p-1

def qsort(a, s, e):
    print "list :", a, "start = ", s , "end = ", e
    if (s >= e):
        return
    p = partition(a, s, e)
    print "partition = a[",p, "] = ", a[p]
    qsort(a, s, p-1)
    qsort(a, p+1, e)

    
#list = [10, 2, 3, 33, 53, 0, 534, 35, 67, 1000]
#list = [10, 2]
#list = [10]
list = [-10, 29, 3, 3, 3, 0, 34, 3, 6, 1000]
list = [1,2,3,4,5,6,7,8,9]
list = [9,8,7,6,5,4,3,2,1]


qsort(list, 0, len(list) -1)
print list
