content=70000
other=30000
sever=50000
sub=15
add=0.8
visitors=int(input("please input a the number of visitors: "))
for i in range(0,visitors+1):
    totalrev=i*0.1*sub+i*add
    if visitors<50000: 
        totalcost=content+other+sever
    else:
        totalcost=content+other+sever+0.001*(visitors-50000)
    netincome=totalrev-totalcost
    if netincome>=0:
        print('visitors number=', i)
        break
if netincome<0:
    print("the net income is ",netincome)