import re
phonePattern = re.compile(r'''
    # don't match beginning of string, number can start anywhere
    (\d{3}) # area code is 3 digits
    \D*     # optional separator is any number of non-digits
    (\d{3}) # trunk is 3 digits
    \D*     # optional separator
    (\d{4}) # rest of number is 4 digits
    \D*     # optional separator
    (\d*)   # extension is optional and any number of digits
    $       # end of string
    ''', re.VERBOSE)

# phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
phonePattern.search('work 1-(800) 555.1212 #1234').groups()
phonePattern.search('800-555-1212')
phonePattern.search('80055512121234')

re.search(r"[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$","micheal.pages@mp.com")