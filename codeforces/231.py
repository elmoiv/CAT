# https://codeforces.com/problemset/submission/231/70400886

import sys

print(sum([i.count('1') > 1 for i in sys.stdin.readlines()[1:]]))