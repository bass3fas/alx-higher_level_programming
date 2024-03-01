#!/usr/bin/python3
import sys
import urllib.request
"""takes in a URL, sends a request to the URL and displays the value
   of the X-Request-Id variable found in the header of the response."""


if __name__ == "__main__":
    url = sys.argv[1]
    html = urllib.request.Request(url)
    with urllib.request.urlopen(html) as response:
        html_id = response.getheader('X-Request-Id')
        print(html_id)
