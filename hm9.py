def get(num):
    if(num>=1):
        res=num+get(num-1)
    else:
        res=0
    return res

cnt=get(10)
print(cnt)
    
