# https://codeforces.com/problemset/submission/158/70418980

import sys

a, b, s = *map(str.split, sys.stdin.readlines()), 0

while (s < int(a[1]) and int(b[s])):
    if s == int(a[1]) - 1:
        s += b[s:].count(b[s])
        break
    s += 1

print(s)