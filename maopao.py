import  random

'''冒泡的排序:对于n个单位长度的列表 需要经过1/2n(n-1). 复杂度为O(N**2)'''
a_list = list(range(1,100))
ready_sort_list = random.sample(a_list,35)

# ready_sort_list =[1,23,4,5,90,32,21,5,88,23,77,59]
for j in range(1,len(ready_sort_list)):  #n 长度的列表  需要经过n-1次 冒泡
    for i in range(len(ready_sort_list) - j):
        if ready_sort_list[i] > ready_sort_list[i + 1]:
            ready_sort_list[i], ready_sort_list[i + 1] = ready_sort_list[i + 1], ready_sort_list[i]
print(ready_sort_list)