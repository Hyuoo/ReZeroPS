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
