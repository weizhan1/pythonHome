from pythonds.basic.deque import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))

from collections import deque
def palchecker(aString):
    chardeque = deque()

    for ch in aString:
        chardeque.append(ch)

    stillEqual = True

    while len(chardeque) > 1 and stillEqual:
        first = chardeque.popleft()
        last = chardeque.pop()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
