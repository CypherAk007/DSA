def mazecnt(r,c):
    if r==1 or c==1:
        return 1
        
    left=mazecnt(r-1,c)
    right=mazecnt(r,c-1)
    return left+right
    
print(mazecnt(4,4))
