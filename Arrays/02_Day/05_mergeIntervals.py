def merge(intervals):
    out =[]
    if len(intervals)<=1:
        return intervals
    intervals.sort()
    
    temp=intervals[0]
    # print(temp)
    for i in intervals:
        print(i)
        if temp[1]>=i[0]:
            print(f'1{temp[1],i[0]}')
            temp[1]=max(temp[1],i[1])
            print(f'01{temp}')
        else:
            print(f'2{temp[1],i[0]}')
            out.append(temp)
            temp=i
            print(f'02{temp}')
    out.append(temp)
    print(out)
    return out
    
a =  [[1,4],[4,5]]
merge(a)