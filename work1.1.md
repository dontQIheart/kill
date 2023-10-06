"""
冒泡
x = int(input('请输入一个整数:'))
y = int(input('请输入一个整数:'))
z = int(input('请输入一个整数:'))
arr = [x,y,z]
def sort1(arr):
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = 1
        if not flag:
            break
sort1(arr)
print(arr)
"""
"""
选择

x = int(input('请输入一个整数:'))
y = int(input('请输入一个整数:'))
z = int(input('请输入一个整数:'))
arr = [x,y,z]
def sort2(arr):
    n = len(arr)
    for i in range(n-1):
        max = i
        for j in range(i+1,n):
            if arr[max]<arr[j]:
                max = j
                arr[i],arr[j] = arr[j],arr[i]
sort2(arr)
print(arr)
"""
"""
折半
x = int(input('请输入一个整数:'))
y = int(input('请输入一个整数:'))
z = int(input('请输入一个整数:'))
arr = [x,y,z]
def sort3(arr):
    n = len(arr)
    for i in range(1,len(arr)):
        T = arr[i]
        j = i-1
        while j>=0 and arr[j]<T:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = T
sort3(arr)
print(arr)
"""