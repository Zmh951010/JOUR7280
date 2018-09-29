import random
numbers=list(range(1,50))
m=int(input("自选数字请按1，机选数字请按2："))
if m==1:
    str1=input("请输入六个1-50之间的整数，用逗号隔开：")
    list1=int(str1.split(','))
    list1.sort()
    print(list1)
else:
    list2=random.sample(numbers,6)
    list2.sort()
    print(list2)
result=random.sample(numbers,6)
result.sort()
special=random.choice(result)
print("搅出号码为：",result,"其中，特别号码为：",special)