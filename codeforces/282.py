# https://codeforces.com/problemset/submission/282/70400233

import sys

print(sum([1 if '+' in i else -1 for i in sys.stdin.readlines()[1:]]))