#Python 3 code to demonstrate

#find intersection of nested list

test_list1=[[1,2],[3,4],[5,6]]
test_list2=[[3,4],[5,7],[1,2]]

print("The original list1:"+str(test_list1))

print("The original list1:"+str(test_list2))

res_list=[]
for i in test_list1:
    if i in test_list2:
        res_list.append(i)
        print("The intersection of two list is :"+str(res_list))

#OUTPUT
The original list1:[[1, 2], [3, 4], [5, 6]]
The original list1:[[3, 4], [5, 7], [1, 2]]
The intersection of two list is :[[1, 2]]
The intersection of two list is :[[1, 2], [3, 4]]
