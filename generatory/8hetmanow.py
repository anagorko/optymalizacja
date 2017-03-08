#!/usr/bin/python

print "Maximize "
f = True
for x in range(ord('a'), ord('h') + 1):
    for y in range(1, 8 + 1):
        if f:
            f = False
        else:
            print '+',
        print chr(x) + str(y),
