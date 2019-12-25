import random
import datetime

time=datetime.datetime.now()

#This point [[ooo]-xxx-xxxx]
numset1 = ['081', '087', '091', '095', '097', '061', '062', '063', '098', '084']
first = random.choice(tuple(numset1))

#This point [xxx-[ooo]-xxxx]
num1 = random.randint(100,999)

#This point [xxx-xxx-[oooo]]
numset2 = {6375, 9191 , 4141, 4545, 2929, 9669, 6969}
num2 = random.choice(tuple(numset2))

print('This is your phone number')
print(first, num1, num2)
#time stamp
print('Generated on', time.strftime("%d %b %Y | %H:%M"))