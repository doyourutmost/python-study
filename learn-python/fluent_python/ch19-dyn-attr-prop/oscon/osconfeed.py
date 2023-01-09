"""
osconfeed.py: Script to download the OSCON schedule feed

# BEGIN OSCONFEED_DEMO

     53 venues
    >>> feed['Schedule']['speakers'][-1]['name']  # <4>
    'Carina C. Zona'
    >>> feed['Schedule']['speakers'][-1]['serial']  # <5>
    141590
    >>> feed['Schedule']['events'][40]['name']
    'There *Will* Be Bugs'
    >>> feed['Schedule']['events'][40]['speakers']  # <6>
    [3471, 5199]


# END OSCONFEED_DEMO
"""

import json
import os
import warnings
# BEGIN OSCONFEED
from urllib.request import urlopen

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)  # <1>
        with urlopen(URL) as remote, open(JSON, 'wb') as local:  # <2>
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)  # <3> json.load 函数解析 JSON 文件，返回 Python 原生对象


if __name__ == '__main__':
    feed = load()
    print(sorted(feed['Schedule'].keys()))
    for key, value in sorted(feed['Schedule'].items()):
        print('{:3} {}'.format(len(value), key))

    print(feed['Schedule']['speakers'][-1]['name'])
    print(feed['Schedule']['speakers'][-1]['serial'])
    print(feed['Schedule']['events'][40]['name'])
    print(feed['Schedule']['events'][40]['speakers'])

