#!/usr/bin/python
import sys
import re

args = sys.argv
replase = False
if ("-i" in args):
    replase = True
    args.remove("-i")

f = open(args[1], 'r')
data = f.read()
f.close()

i = 1
pattern = "(.*=[ \t\n\r\f\v]*)([0-9]+)(.*)"
r = re.compile(pattern)

data = data.replace("=\n", "=")

if (replase):
    f = open(args[1], 'w')

for line in data.split('\n'):
    m = r.match(line)
    if (m):
        if (replase):
            f.write(m.group(1) + repr(i) + m.group(3) + '\n')
        else:
            print (m.group(1) + repr(i) + m.group(3))

        i += 1
    else:
        if (replase):
            f.write(line + '\n')
        else:
            print(line)

    if (re.match('^\s*message', line)):
        i = 1
    elif (re.match('^\s*enum', line)):
        i = 0
