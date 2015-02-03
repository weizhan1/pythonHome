regex = re.compile(

    r'^(?:http|ftp)s?://' # http:// or https://

    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...

    r'localhost|' # localhost...

    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4

    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6

    r'(?::\d+)?' # optional port

    r'(?:/?|[/?]\S+)$', re.IGNORECASE)



from django.core.validators import URLValidator

from django.core.exceptions import ValidationError

val = URLValidator(verify_exists=False)

try:

    val('http://www.google.com')

except ValidationError, e:

    print e

regex = re.compile(

        r'^(?:http|ftp)s?://' # http:// or https://

        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...

        r'localhost|' #localhost...

        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip

        r'(?::\d+)?' # optional port

        r'(?:/?|[/?]\S+)$', re.IGNORECASE)



import urllib2 

def file_exists(location):

    request = urllib2.Request(location)

    request.get_method = lambda : 'HEAD'

    try:

        response = urllib2.urlopen(request)

        return True

    except urllib2.HTTPError:

        return False



import httplib

c = httplib.HTTPConnection('www.abc.com')

c.request("HEAD", '')

if c.getresponse().status == 200:

   print('web site exists')

or you can use urllib2



import urllib2

try:

    urllib2.urlopen('http://www.abc.com/some_page')

except urllib2.HTTPError, e:

    print(e.code)

except urllib2.URLError, e:

    print(e.args)

>>> import httplib

>>>

>>> def exists(site, path):

...     conn = httplib.HTTPConnection(site)

...     conn.request('HEAD', path)

...     response = conn.getresponse()

...     conn.close()

...     return response.status == 200

...

>>> exists('http://www.fakedomain.com', '/fakeImage.jpg')

False



import requests

def exists(path):

    r = requests.head(path)

    return r.status_code == requests.codes.ok

print exists('http://www.fakedomain.com/fakeImage.jpg')



import urllib2

import re

def is_fully_alive(url, live_check = False):

    try:

        if not urllib2.urlparse.urlparse(url).netloc:

            return False

        website = urllib2.urlopen(url)

        html = website.read()

        if website.code != 200 :

            return False

        # Get all the links

        for link in re.findall('"((http|ftp)s?://.*?)"', html):

            url = link[0]

            if not urllib2.urlparse.urlparse(url).netloc:

                return False

            if live_check:

                website = urllib2.urlopen(url)

                if website.code != 200:

                    print "Failed link : ", url

                    return False

    except Exception, e:

        print "Errored while attempting to validate link : ", url

        print e

        return False

    return True



from urllib2 import urlopen

code = urlopen("http://example.com/").code

if (code / 100 >= 4):

   print "Nothing there.”



import urllib2

ret = urllib2.urlopen('http://hostname/directory/file.jpg')

if ret.code == 200:

    print "Exists!”

import httplib

import urlparse

def get_server_status_code(url):

    """

    Download just the header of a URL and

    return the server's status code.

    """

    # http://stackoverflow.com/questions/1140661

    host, path = urlparse.urlparse(url)[1:3]    # elems [1] and [2]

    try:

        conn = httplib.HTTPConnection(host)

        conn.request('HEAD', path)

        return conn.getresponse().status

    except StandardError:

        return None

 

def check_url(url):

    """

    Check if a URL exists without downloading the whole file.

    We only check the URL header.

    """

    # see also http://stackoverflow.com/questions/2924422

    good_codes = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]

    return get_server_status_code(url) in good_codes

import httplib

import urlparse

def httpExists(url):

    host, path = urlparse.urlsplit(url)[1:3]

    found = 0

    try:

        connection = httplib.HTTPConnection(host)  ## Make HTTPConnection Object

        connection.request("HEAD", path)

        responseOb = connection.getresponse()      ## Grab HTTPResponse Object

        if responseOb.status == 200:

            found = 1

        else:

            print "Status %d %s : %s" % (responseOb.status, responseOb.reason, url)

    except Exception, e:

        print e.__class__,  e, url

    return found

def _test():

    import doctest, httpExists

    return doctest.testmod(httpExists)

if __name__ == "__main__":

    _test()

