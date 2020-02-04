# https://codeforces.com/problemset/submission/112/70319201

import sys

z = list(map(str.lower, sys.stdin.readlines()))
print(int((z == sorted(z)[::-1]) or - (z == sorted(z))) * (len(set(z)) > 1))