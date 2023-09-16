'''
import time
import numpy

count = 1234
tt=[]
for i in range(20):
    start = time.time()
    for _ in range(count):

        ## <TEST_CODE> ##

    tt.append(time.time() - start)
    print(i,"..",end=" ")
print("\n속도 >>", sum(tt)/len(tt))
#print("표준편차 : {}\tM : {}\tm : {}".format(round(numpy.std(tt),6),round(max(tt),6),round(min(tt),6)))
'''

import time

def runtime(func):
    def deco():
        start = time.time()
        func()
        end = time.time()
        print(f"{func.__name__}() runtime: {end-start}seconds")
    return deco

def loop_test(func):
    LOOP_COUNT = 100000
    def deco():
        start = time.time()
        for i in range(10):
            print(i, end="")
            for _ in range(LOOP_COUNT):
                func()
        print()
        end = time.time()
        print(f"{LOOP_COUNT*10} loops, {func.__name__}() runtime: {end-start}seconds")

    return deco


# 20000000 loops, best of 5: 12.3 nsec per loop