def count(s,idx,c):
    if idx==len(s):
        return c
    print(s[idx])
    x=count(s,idx+1,c+1)
    return x
    
if __name__ == '__main__':
    s=input()
    out=count(s,0,0)
    print(out)