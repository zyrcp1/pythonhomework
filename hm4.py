#将字符串去重且从小到大排序

s='ajldjlajfdljfddd'
s=set(s)
s=list(s)
s.sort(reverse=False)
res="".join(s)
print(res)
