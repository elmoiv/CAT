# https://codeforces.com/problemset/submission/96/70316506

import re

print(['YES', 'NO'][len(re.split(r'0{7}|1{7}', input())) == 1])