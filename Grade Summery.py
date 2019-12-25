n = input('Enter Score:')
# Error sting 
score = int(n)
# Fix Error n = int  or n = score.int


if score>=80 and score<=100:
   print('คะแนน',score,'ได้เกรด 4')
elif score>=75 and score<=79:
   print('คะแนน',score,'ได้เกรด 3.5')
elif score>=70 and score<=74:
   print('คะแนน',score,'ได้เกรด 3')
elif score>=65 and score<=69:
   print('คะแนน',score,'ได้เกรด 2.5')
elif score>=60 and score<=64:
   print('คะแนน',score,'ได้เกรด 2')
elif score>=55 and score<=59:
   print('คะแนน',score,'ได้เกรด 1.5')
elif score>=50 and score<=54:
   print('คะแนน',score,'ได้เกรด 1')
elif score>=0 and score<=49:
   print('คะแนน',score,'ได้เกรด 0')
else:
   print('ERR: Please enter score as a number only')