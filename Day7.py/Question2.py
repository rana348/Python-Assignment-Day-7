#summation of tuples in list
#initialize list of tuple

test_list=[(1,3),(5,6,7),(2,6)]

print("The original list:"+str(test_list))

res=sum(map(sum,test_list))

print("The summation of all tuple elements are:"+str(res))


#OUTPUT
The original list:[(1, 3), (5, 6, 7), (2, 6)]
The summation of all tuple elements are:30