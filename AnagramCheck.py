# O(n**2)
def anagramSolution(s1, s2):
    alist = list(s2)
    pos1 = 0
    stillOK = True
    
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2+1
                
        if found:
            alist[pos2] = None
        else:
            stillOK= False
            
        pos1 = pos1+1
        
    return stillOK
    
print(anagramSolution1('abcd','dcba'))

# O(nlogn)
def anagramSolution2(s1,s2):
     alist1 = list(s1)
     alist2 = list(s2)
     
     alist1.sort()
     alist2.sort()
     
     pos = 0
     matches = True
     
     while pos < len(s1) and matches:
        if alist1[pos]==alist[pos]:
            pos = pos+1
        else:
            matches = False
            
    return matches
    
print(anagramSolution2('abcde','edcba'))

'''
A brute force technique for solving a problem typically tries to exhaust all possibilities. For the anagram detection problem, we can simply generate a list of all possible strings using the characters from s1 and then see if s2 occurs. However, there is a difficulty with this approach. When generating all possible strings from s1, there are n possible first characters, n−1 possible characters for the second position, n−2 for the third, and so on. The total number of candidate strings is n∗(n−1)∗(n−2)∗...∗3∗2∗1, which is n!. Although some of the strings may be duplicates, the program cannot know this ahead of time and so it will still generate n! different strings.

It turns out that n! grows even faster than 2n as n gets large. In fact, if s1 were 20 characters long, there would be 20!=2,432,902,008,176,640,000 possible candidate strings. If we processed one possibility every second, it would still take us 77,146,816,596 years to go through the entire list. This is probably not going to be a good solution.
'''

# O(n)
def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    
    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos]+1
        
    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos]+1
        
    j = 0
    stillOK = True
    
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j=j+1
        else:
            stillOK = False
            
    return stillOK
    
print(anagramSolution4('apple','pleap'))
    
               