>>> my_list = [1, 7, 11, 8, 13, 2]
>>> [("odd","even")[i % 2 == 0] for i in my_list]
["odd","odd","odd","even","odd","even"]
A more useful example would be to threshold a list of data:

thresholded_data = [(0,1)[i > threshold] for i my_list]
But in that situation, it's easier to just coerce the test into an integer:

thresholded_data = [int(i > threshold) for i my_list]


my_string = "I want to get the counts for each letter in this sentence"
counts = {}

for letter in my_string:
    counts[letter] = counts.get(letter, 0) + 1
print counts

import regex as re
re_zeros = re.compile('\.(\d*?)(0+)$')
Then given a string that has been formatting, it is searched for trailing zeros. The string is truncated by the number of trailing zeros, and if there aren't any other digits after the decimal place, it is truncated by a further place to remove the decimal place.

z = re_zeros.search(str_n)
if z:
  length = (len(z.group(2)) + (len(z.group(1)) == 0))
  str_n = str_n[:-length]

>>> sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

>>> student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

>>> class Student:
        def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
        def __repr__(self):
                return repr((self.name, self.grade, self.age))
        def weighted_grade(self):
                return 'CBA'.index(self.grade) / float(self.age)

>>> student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]
>>> sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

if n < 0:
    result = 'n is negative'
else:
    result = 'n is positive'
You can write:

result = n < 0 and 'n is negative' or 'n is positive'
The result is shorter, though I'm not sure it's more readable. However, the fact that it's a single line makes it more versatile. For example, you can include it in a list comprehension, as I did in this contrived example, or you can pass it as an argument to a function.

Then general form is:

result = test and true_result or false_result
The logic is that the two results count as being true, so if the test is true, then test and true_result is true; if the test is false then test or false_result is true.

ls -al | grep ^d
find . -type f ! -name '*.txt' -delete
cat /dev/null > ~/.bash_history && history -c && exit

1. Emulating "?:"
Python doesn't know the trinary operator "?:" from C. However, it's pretty easy to emulate:

x ? y : z    -->    [z, y][bool(x)]

(If you're sure that x is already a boolean type (or an integer of value 0 or 1), you can omit the bool() function, of course.)

How does the trick work? We simply create a small list constant, containing the two values to choose from, and use the boolean as an index into the list. "False" is equivalent to 0 and will select the first element, while "True" is equivalent to 1 and will select the second one.

Note that always all three operands will be evaluated, unlike the "?:" operator in C. If you need shortcut evaluation, use an if-else statement.

Actually, there's another way to do it with shortcut evaluation, but it only works if y does not contain a boolean False equivalent:

x ? y : z    -->    bool(x) and y or z

2. Checking the Python version
You will often find yourself using features that are not available in older versions of Python. If someone happens to run your program with a too old version, an ugly exception traceback will be printed which is usually not very helpful to the user. Better use a snippet like this:

import sys
if not hasattr(sys, "hexversion") or sys.hexversion < 0x020300f0:
    sys.stderr.write("Sorry, your Python is too old.\n")
    sys.stderr.write("Please upgrade at least to 2.3.\n")
    sys.exit(1)

Those lines should be at the very top of your program, even before any other import statements. The variable hexversion is only available since Python 1.5.2, so we first check if it is there, just in case someone has an even older version. The format of the variable is 0x<maj><min><rev><rel> (major, minor and revision number, and an indication of the release status, which is f0 for official final releases). Each of the four parts is two hexadecimal digits.

3. Debugging CGIs
The "cgitb" module (available since Python 2.2) is extremely helpful when debugging CGI programs. Whenever a run-time error (i.e. exception) occurs, a nicely formatted HTML fragment will be produced, containing the backtrace with source context, line numbers and even contents of the variables involved. To use this module, put this line somewhere at the top of your CGI program:

import cgitb; cgitb.enable()

4. Parallel sorting of lists
Sometimes you want to sort a list, and there's a second list (of the same length) which should be sorted along with it. Of course, you could have used a single list of 2-tuples in the first place, but sometimes a program requires a different structure. Anyway, it's easy. The following snippet works with two or more lists (the example shows only two).

data = zip(list1, list2)
data.sort()
list1, list2 = map(lambda t: list(t), zip(*data))

Note that zip() returns a list of tuples, so you have to convert the result of the last zip() back to lists. That's what the map() command along with the lambda function does. If you don't actually need lists, the last line could be simplified like this:

tuple1, tuple2 = zip(*data)

5. Normalizing a MAC address
I found myself having to convert MAC addresses (sometimes called ethernet address) to a canonical format, i.e. each of the six parts with two digits, and having all lowercase hexadecimal digits. It's quite likely that there is an easier way, but this is what I came up with:

mac = ":".join([i.zfill(2) for i in mac.split(":")]).lower()

(The zfill method of string objects is available since Python 2.2.2.)

6. Sorting IP addresses
How to sort a list of strings that represent IP addresses? Of course, you could supply an appropriate comparison function to the sort() method of the list object, but that's very inefficient (read: slow).

It is better to first pre-process the list so it can be sorted with the efficient built-in comparison function (which simply compares strings character-by-character), and afterwards post-process the sorted list back to the normal format. That trick is applicable to a lot of sorting situations, not just IP addresses.

In the case of IP addresses, we re-format them so that each of the four octets is aligned inside a three-character field (preceded by spaces if necessary). Then all strings will be the same length and can be sorted using the fast built-in comparison function. Afterwards, we simply remove all spaces.

for i in range(len(ips)):
    ips[i] = "%3s.%3s.%3s.%3s" % tuple(ips[i].split("."))
ips.sort()
for i in range(len(ips)):
    ips[i] = ips[i].replace(" ", "")

7. Parsing command line options
This is a code snippet for parsing command line options (using the getopt module) in a sophisticated way. In this example, the program accepts three options (both as one-letter options and as long options) and requires at least two arguments.

import sys, getopt, os.path
me = os.path.basename(sys.argv[0])

debug   = False
really  = True
verbose = False

my_options = (
    ("d", "debug",     "debug   = True",  "Enable debug mode."),
    ("n", "notreally", "really  = False", "No action, display only."),
    ("v", "verbose",   "verbose = True",  "Increase verbosity.")
)

short_opts = reduce(lambda a, b: a + b[0], my_options, "")
long_opts  = map(lambda x: x[1], my_options)

def usage ():
    args = "[-%s] <dir1> <dir2> [...]" % short_opts
    print >> sys.stderr, "Usage: ", me, args, "\nOptions:"
    for opt in my_options:
        print >> sys.stderr, "-" + opt[0], opt[3]
    sys.exit(1)

try:
    opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
except getopt.GetoptError:
    usage()

for o, p in opts:
    for shrt, lng, action in my_options:
        if o[1:] in shrt or o[2:] == lng:
            exec action
            break
    else:
        usage()

if len(args) < 2:
    usage()

8. Mixing Python and shell scripts
Sometimes it might be useful to write a script that can be used as a shell script or as a Python script at the same time. This is possible. The trick is that a sequence of four quote characters means an empty string to the shell, but in Python it starts a triple-quoted string that begins with a quote character. So you can embed shell commands within that triple-quoted string. Note that the first string in a module or script is simply stored as the doc string for that module, but other than that it is simply ignored by the Python interpreter.

The following example demonstrates that trick. It is started as a shell script (because of the #!/bin/sh line). The embedded shell commands check if Python is installed. If not, a useful error message is displayed and the script exits. Otherwise, if Python is found, the script is re-executed with it. Python ignores the triple-quoted doc string and executes the rest like a normal Python program.

If you want to have a a real doc string for your program, you will have to assign it afterwards. The script below shows how to do this, too.

#!/bin/sh

"""":
if which python >/dev/null; then
    exec python "$0" "$@"
else
    echo "${0##*/}: Python not found. Please install Python." >&2
    exit 1
fi
"""

__doc__ = """
Demonstrate how to mix Python + shell script.
"""

import sys
print "Hello World!"
print "This is Python", sys.version
print "This is my argument vector:", sys.argv
print "This is my doc string:", __doc__
sys.exit (0)

9. Converting signal numbers to names
Unfortunately there is no existing function in the "signal" module that converts a signal number to a signal name, although that would be a useful thing to have. The following function fills that gap.

import signal

def signal_numtoname (num):
    name = []
    for key in signal.__dict__.keys():
        if key.startswith("SIG") and getattr(signal, key) == num:
            name.append (key)
    if len(name) == 1:
        return name[0]
    else:
        return str(num)


import getopt, sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"
    # ...

if __name__ == "__main__":
    main()
