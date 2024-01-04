#!/usr/bin/python3
for K in range(ord('a'), ord('z') + 1):
    if chr(K) != 'e' and chr(K) != 'q':
        print('{:c}'.format(K), end='')
