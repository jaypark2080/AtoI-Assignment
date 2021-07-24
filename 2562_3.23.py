#2562
# 작성일 : 2021/3/23

num_list=[]

for i in range(9):
    num=int(input())
    num_list.append(num)

print(max(num_list))
print(num_list.index(max(num_list)) + 1)