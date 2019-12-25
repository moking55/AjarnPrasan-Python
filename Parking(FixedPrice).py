import time
timeis = time.localtime()
a = time.strftime('%H''%M', timeis)
#import เวลา
Y = input("do you want parking Y or N")
# ต้องการที่จอดรถไหม
if Y <= Y:
    print("start",a)
else :
    print("ok")
c2 = input("do you want out parking :")
#ออกและระบุเวลา
total = (int(c2) - int(a))
print(total,'min')
#จอดกี่นาที่
if total <= 30:
    print("30 baht")
else:
   print("60 baht")