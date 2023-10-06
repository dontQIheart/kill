s1 = str(input('请输入字符:'))
print(s1)
if 'ol' in s1:
    print('原含有ol,将变化')
    s1 = s1.replace('ol','fzu')
s1 = s1[::-1]
print(s1)
