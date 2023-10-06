'''
list = input("输入：(元素中间请用空格隔开）").split()
'''
list = [1,'xyz',2]
new_list = []
for T in list:
    if isinstance(T,int):
        new_list.append(T)
list = new_list
print(list)
