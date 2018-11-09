#__author:yewei
#__date :2018-11-06
#__name:根据利润对应计算奖金
while(True):
    i=int(input('利润：'))
    arr=[1000000,600000,400000,200000,100000,0]
    arr2=[0.01,0.015,0.03,0.05,0.075,0.1]
    r=0
    for x in range(0,6):
        if i>arr[x]:
            r+=(i-arr[x])*arr2[x]
            i=arr[x]
    print('奖金为：'+r)