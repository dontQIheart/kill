scores = { 522: 'ikun', 523: '雪', 524: '泰酷辣',525: '快乐'}
print(scores)
for i in list(scores.keys()):
    if i%2 == 0:
        del(scores[i])
print('更改完毕')
print(scores)
