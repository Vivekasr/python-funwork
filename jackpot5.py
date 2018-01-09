import random

a = int(input('Enter your birthdate:'))
b = int(input('Enter your lucky number:'))
c = a*b
P = c*random.randint(1,9)
yournum = P%10

if yournum == 1 or yournum == 9:
    print('Well you get a free beer from us :)')

if yournum == 2  or yournum == 8:
    print('Some luck is with you :) you won special10 coupon!')

if yournum == 3  or yournum == 7:
    print('lucky you won special refill code 1234jackpot5')

if yournum == 4  or yournum == 6:
    print('wow so close for jackpot :O')
    print('You won BONUS!:)')

if yournum == 5:
    print('CONGRATULATIONS!! :)')
    print('You won JACKPOT!!!!!')

if yournum==0:
    print('your luck took you to ZERO :(')

print('THANK YOU for playing go to counter to collect your win :)')
