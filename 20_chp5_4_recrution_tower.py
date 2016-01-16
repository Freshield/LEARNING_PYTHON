def hannuo_tower(number,a,b,c):

    if number==1:
        print('move',a,'-->',c)
        return

    hannuo_tower(number-1,a,c,b)

    print('move',a,'-->',c)
    
    hannuo_tower(number-1,b,a,c)

hannuo_tower(5,'A','B','C')











