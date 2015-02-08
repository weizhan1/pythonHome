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

>>> first_chars = [word[0] for word in itertools.takewhile(lambda word: word != "and", text.split())]

from itertools import groupby

def get_category(line):
    return line.split("/")[0]

with open("/var/lib/portage/world") as worldfile:
    packages = {category: list(packages) for category, packages in groupby(worldfile, get_category)}
