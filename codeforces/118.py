# https://codeforces.com/problemset/submission/118/70319427

# Python 2.7
print('.'.join([''] + list(raw_input().lower().translate(None, 'aeiouy'))))