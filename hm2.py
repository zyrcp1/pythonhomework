#字典如何删除键和合并两个字典
dic={"name":"xx","age":18}
del dic["name"]
print(dic)
dic1={"name":"yy"}
dic.update(dic1)
print(dic)