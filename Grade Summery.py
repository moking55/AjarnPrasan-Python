while True:
   score = int(input('Enter Score:'))
   if score>=80 and score<=100:
      print('คะแนน',score,'ได้เกรด 4')
      break
   elif score>=75 and score<=79:
      print('คะแนน',score,'ได้เกรด 3.5')
      break
   elif score>=70 and score<=74:
      print('คะแนน',score,'ได้เกรด 3')
      break
   elif score>=65 and score<=69:
      print('คะแนน',score,'ได้เกรด 2.5')
      break
   elif score>=60 and score<=64:
      print('คะแนน',score,'ได้เกรด 2')
      break
   elif score>=55 and score<=59:
      print('คะแนน',score,'ได้เกรด 1.5')
      break
   elif score>=50 and score<=54:
      print('คะแนน',score,'ได้เกรด 1')
      break
   elif score>=0 and score<=49:
      print('คะแนน',score,'ได้เกรด 0')
      break
   else:
      print('ERR: ห้ามป้อนคะแนนเกิน 100 คะแนน')
      continue