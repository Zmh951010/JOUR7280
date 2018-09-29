r = float(input('please input the yearly interest rate:'))/12
n = int(input('please input the number of year:'))*12
P = float(input('please input the principal in HKD:'))
A = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
outstanding = P
row0 = '{0} \t {1} \t {2} \t {3} \t {4}'.format('month','instalment','interest','principal','outstanding')
print(row0)
month = 1
for m in range(1, n+1):
    interest = outstanding * r
    principal = A - interest
    outstanding = outstanding - principal
    print('{0:04d} \t {1:.2f} \t {2:.2f} \t {3:.2f} \t {4:.2f}'.format(month,A,interest,principal,outstanding))
    month = month+1