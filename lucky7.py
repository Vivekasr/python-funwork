#lucky_7
#three number print if 777 u win if koi 2 num same so bonus
#three numbers should be random
import random
yesorno = input('Are you to play the game?')
if yesorno == ('yes'):
    print('enjoy your number')
    num1,num2,num3 = random.randint(6,9),random.randint(5,8),random.randint(2,8)
    print(num1,num2,num3)

else:
    print("jackpot don't want you either")

if num1==num2==num3==7:
    print('You won the jackpot!!!!')

elif num1==num2 or num2==num3 or num1==num3 :
    print('You won the bonus!!')

if num1!=num2!=num3!=num1:
    print('Luck is not with you this time :(')
