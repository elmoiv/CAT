# https://codeforces.com/contest/71/submission/70216589

import sys

print(*(f'{w[0]}{len(w) - 3}{w[-2]}' if len(w) > 11 else w for w in sys.stdin.readlines()[1:]))