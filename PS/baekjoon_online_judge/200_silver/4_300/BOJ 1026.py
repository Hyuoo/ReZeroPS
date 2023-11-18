input()
print(sum(map(lambda x:(x[0]*x[1]),(zip(sorted(map(int,input().split())),sorted(map(int,input().split()),reverse=True))))))
