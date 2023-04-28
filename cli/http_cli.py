#!/usr/bin/python3

# TODO: clean up and add features (body, HTTPS, etc.)

import sys
from http.client import HTTPConnection, HTTPResponse, HTTP_PORT

def get_response(method: str, protocol: str, host: str, url: str) -> HTTPResponse:
    if (protocol != "http"):
        raise ValueError("Only HTTP is supported")
    connection: HTTPConnection = HTTPConnection(host, HTTP_PORT)
    connection.request(method, url)
    response: HTTPResponse = connection.getresponse()
    return response

def parse_protocol(url: str) -> str:
    return url.split(':')[0]

def parse_hostname(url: str) -> str:
    return [_ for _ in url.split(':')[1].split('/') if _ != ''][0]

def parse_url(url: str) -> str:
    lst: list = [_ for _ in url.split(':')[1].split('/') if _ != '']
    lst.pop(0)
    result: str = '/'
    for c in lst:
        result += c
        result += '/'
    return result

def get_headers_str(res: HTTPResponse) -> str:
    result: str = "HTTP " + str(res.getcode()) + '\n'
    headers: list = res.getheaders()
    for t in headers:
        result += (t[0] + ': ' + t[1] + '\n')
    return result

def get_body_str(res: HTTPResponse) -> str:
    try:
        for h in res.getheaders():
            if h[0] == "Content-Type":
                if "charset=" in h[1].split(';')[1]:
                    encoding: str = h[1].split(';')[1].split("=")[1]
    except:
        encoding: str = "utf-8"
    result: str = ''
    for line in res.readlines():
        result += (line.decode(encoding))
    return result

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please provide the method and the URL")
    else:
        method: str = sys.argv[1]
        url: str = sys.argv[2]
        res: HTTPResponse = get_response(method, parse_protocol(url), parse_hostname(url), parse_url(url))
        print(get_headers_str(res))
        print()
        print(get_body_str(res))
