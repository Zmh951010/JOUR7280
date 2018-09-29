# the basic logic is 'net income = total revenue - total cost'
# first of all, we need set the cost, which include 3 parts, the content cost, other cost, and server cost
content=70000
other=30000
sever=50000 # also, if the number of visitors is larger than 50000, there will be additional clouds fees
# now for the revenue
sub=15
add=0.8
# now we need to set the number of visitors
visitors=int(input("please input a the number of visitors: "))
totalrev=visitors*0.1*sub+visitors*add
if visitors<50000: 
    totalcost=content+other+sever
    netincome=totalrev-totalcost
else:
    totalcost=content+other+sever+0.001*(visitors-50000)
    netincome=totalrev-totalcost
print("the net income is ",netincome)