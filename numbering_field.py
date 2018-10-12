#!/usr/bin/python
import sys
import re

args = sys.argv
f = open(args[1])
data = f.read()
f.close()

i = 1
pattern = "(.*=[ \t\n\r\f\v]*)([0-9]+)(.*)"
r = re.compile(pattern)

data = data.replace("=\n", "=")

for line in data.split('\n'):
    m = r.match(line)
    if (m):
        print (m.group(1) + repr(i) + m.group(3))
        i += 1
    else:
        print(line)

    if (re.match('^message', line)):
        i = 1
