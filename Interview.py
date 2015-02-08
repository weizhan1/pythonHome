import collections

with open(‘intCnt.txt’, ‘r’) as f:
 for line in f: 
  mapCnt2 = collections.Counter([])
  list = line.split()
  mapCnt = collections.Counter(list)
  mapCnt.most_common(1)
  mapCnt2 += mapCnt

 A = Counter({2: 2, 1: 1, 3: 1})
 B = Counter({2: 2, 1: 1, 3: 1})

 A + B = {2: 4, 1: 2, 3: 2}
