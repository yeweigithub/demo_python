#__author:yewei
#__date :2018-11-06
#__name: 1，2，3，4 不重复组合
for i in range(1,5):
    for k in  range(1,5):
        for j in range(1,5):
            if i!=k and k!=j and j!=i :
                print (i,k,j)