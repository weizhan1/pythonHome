def sequentialSearch(alist, item):
2        pos = 0
3        found = False
4    
5        while pos < len(alist) and not found:
6            if alist[pos] == item:
7                found = True
8            else:
9                pos = pos+1
10    
11        return found
12    
13    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
14    print(sequentialSearch(testlist, 3))
15    print(sequentialSearch(testlist, 13))

def orderedSequentialSearch(alist, item):
2        pos = 0
3        found = False
4        stop = False
5        while pos < len(alist) and not found and not stop:
6            if alist[pos] == item:
7                found = True
8            else:
9                if alist[pos] > item:
10                    stop = True
11                else:
12                    pos = pos+1
13    
14        return found
15    
16    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
17    print(orderedSequentialSearch(testlist, 3))
18    print(orderedSequentialSearch(testlist, 13))