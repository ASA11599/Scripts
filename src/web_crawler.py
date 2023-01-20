#!/usr/bin/python3

import requests as rqs
import os
import sys
import html.parser as hp
from queue import Queue
import re


regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def is_url(url: str) -> bool:
    return (re.match(regex, url) is not None)


class MyHTMLParser(hp.HTMLParser):

    q: Queue = Queue(0)

    def handle_starttag(self, tag, attrs):
        for attr_t in attrs:
            if attr_t[0] == 'href':
                if is_url(attr_t[1]):
                    MyHTMLParser.q.put(attr_t[1])
                    print("Found link to: " + str(attr_t[1]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a URL")
    else:
        if not is_url(sys.argv[1]):
            print("Please provide a valid URL")
        else:
            MyHTMLParser.q.put(sys.argv[1])
            while not MyHTMLParser.q.empty():
                try:
                    res: rqs.Response = rqs.get(MyHTMLParser.q.get())
                    parser: hp.HTMLParser = MyHTMLParser()
                    parser.feed(res.text)
                except Exception as e:
                    print("Something went wrong...")
                    print(e)
