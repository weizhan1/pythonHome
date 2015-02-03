def multipliers():
    return [lambda x : i * x for i in range(4)]
    
print [m(2) for m in multipliers()]

def multipliers():
     for i in range(4): yield lambda x : i * x 
     
def multipliers():
    return [lambda x, i=i : i * x for i in range(4)]
    
    
from functools import partial
from operator import mul

def multipliers():
    return [partial(mul, i) for i in range(4)]
