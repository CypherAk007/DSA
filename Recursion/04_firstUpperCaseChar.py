def findfstup(string,idx):
    if idx==len(string)-1:
        return -1
    if ord(string[idx])>=65 and ord(string[idx])<=90:
        return string[idx]
    else:
        fica=findfstup(string,idx+1)
        return fica


string='geeksforgeeKs'
idx=0
print(findfstup(string,idx))