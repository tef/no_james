#!/usr/bin/env python
from pandocfilters import toJSONFilter, Link
import sys

def fix_link(url):
    return "lol"

def walk(key, value, format, meta):
    if key == 'Link':
        value[1][0] = fix_link(value[1][0])
        return {'t': key, 'c': value}

if __name__ == "__main__":
    toJSONFilter(walk)
