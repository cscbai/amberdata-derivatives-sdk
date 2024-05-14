# ======================================================================================================================

import re
import requests
import unittest
from urllib.parse import urlparse


# ======================================================================================================================

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


# ======================================================================================================================

class ValidateLinksTestCase(unittest.TestCase):
    def test_links(self):
        with open('README.md', 'r') as f:
            content = f.read()

        # This does not handle multiple links in the same string
        # match = re.search("(?P<url>https?://[^\s]+)", content)
        # if match is not None:
        #     print(match.group("url"))

        # This handles multiple links in the same string, but requires to fist split it.
        # lines = [item for item in content.split(" ")]
        # for item in lines:
        #     match = re.search("(?P<url>https?://[^\s]+)", item)
        #     if match is not None:
        #         print('link:', match.group("url"))

        # This only extracts hostnames
        # urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', content)

        # This regex works on multiline strings - inspired from https://www.geeksforgeeks.org/python-check-url-string/
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        urls = re.findall(regex, content)
        urls = [x[0] for x in urls]                          # Keep only the URLs
        urls = list(filter(lambda x: is_valid_url(x), urls)) # Keep only well-formed URLs
        urls = list(set(urls))                               # Unique the list of URLs

        for url in urls:
            response = requests.get(url)
            self.assertEqual(response.status_code, 200, 'URL ' + url + ' does not exist.')


# ======================================================================================================================

if __name__ == '__main__':
    unittest.main()

# ======================================================================================================================
