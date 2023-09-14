T = int(input())
#룩이 8개가 안겹치게 체스판에 들어갔는지 체크하는 문제
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    ans=1
    check = [0 for i in range(8)]
    for i in range(8):
        line = input()
        if(line.count("O")==1):
           check[line.index("O")] = 1
        else:
           ans=0
    print("#{0} {1}".format(test_case, "yes" if check.count(0)==0 and ans==1 else "no"))
    # ///////////////////////////////////////////////////////////////////////////////////
