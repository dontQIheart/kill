for i in range(1,10):
    for j in range(1,i+1):
        print('%dX%d=%d'%(j,i,i*j),end=' ')
        if j==i:
            print('\t')
