input_dir = "c:/Users/h3/web/xxst/find_elisp/validate matching brackets/xxdir"
input_dir = "c:/Users/h3/web/xahlee_org/p/time_machine"
input_dir = "c:/Users/h3/web/xahlee_org/comp/validate_matching_brackets/xx"

import os, re

def check_balance(characters):
    '''Return -1 if all delimiters are balanced or
       the char number of the first delimiter mismatch.

    '''
    openers = {
        '(': ')',
        '{': '}',
        '[': ']',
        '“': '”',
        '‹': '›',
        '«': '»',
        '【': '】',
        '〈': '〉',
        '《': '》',
        '「': '」',
        '『': '』',
        }
    closers = set(openers.values())
    stack = []
    for i, c in enumerate(characters, start=1):
        if c in openers:
            stack.append(openers[c])
        elif c in closers:
            if not stack or c != stack.pop():
                return i
    if stack:
        return i
    return -1

def scan(directory, encoding='utf-8'):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            fullname = os.path.join(dirpath, filename)
            if re.search(r'\.txt$', filename, re.U) and os.path.isfile(fullname):
                print ( "processing:" + fullname)
                with open(fullname, 'r', encoding=encoding) as f:
                    try:
                        characters = f.read()
                    except UnicodeDecodeError:
                        continue
                position = check_balance(characters)
                if position >= 0:
                    print('{0!r}: {1}'.format(position, fullname))

scan(input_dir)

print ("done")