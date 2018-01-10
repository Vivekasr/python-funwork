n = int(input('Enter the number of fibonacci number you want:'))
count = 0
n1 = 0
n2 = 1
if n<=0:
    print('invalid choose positive')
elif n==1:
    print('0')
elif n==2:
    print('1')
else:    
    while count < n:
       print(n1,end=' ')
       nth = n1 + n2

       n1 = n2
       n2 = nth
       count += 1
