
import sys

def sqrt(i, start, end, tolerance):
    print "entered *****"
    print i, start, end, tolerance
    
    mid = (end - (start))/2.0 + start
    print mid
    if (mid == 0):
        print "returning start"
        return start
    if (abs((mid * mid) - i) <= tolerance):
        print "returning mid ", mid
        return mid
    print "abs is ", abs(mid*mid)
    if (abs(mid * mid) < i):
        print "in case 1"
        return sqrt(i, mid, end, tolerance)
    else:
        print "in case 2"
        return sqrt(i, start, mid, tolerance)


i = float(30)
my_tolerance = 0.01

p = sqrt(i, 0, i, my_tolerance)

print "sqrt is ", p
