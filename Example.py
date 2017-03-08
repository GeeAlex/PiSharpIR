import GP2Y
import math
import sys
import time
while True:
    GP2Y.distcalc()
    lk = GP2Y.Distance
    print("Distance(cm): ", str.format('{0:.2f}',lk))
    time.sleep(1)
    
