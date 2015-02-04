"1a2b3c" = 6
"12fg24" = 36

int sumOfNumbers(String str)
{
}

import re
s = "1a2b3c"
num = re.findall('-\d+|\d+', s)
strint = [int(x) for x in num]
sum(strint)
