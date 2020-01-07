import os, json, time, os.path, pathlib
from datetime import datetime
from os import system, name, path

'''
สงวนลิขสิทธิ์ (c) 2020 เมธาวัฒน์ มหาวัน 
สัญญาอนุญาตครีเอทีฟคอมมอนส์
แสดงที่มา-ไม่ใช้เพื่อการค้า 4.0 International

คุณมีสิทธิที่จะ:

แบ่งปัน - คัดลอกและแจกจ่ายเนื้อหาในสื่อหรือรูปแบบใดก็ได้
ปรับเปลี่ยน - เรียบเรียงใหม่,ดัดแปลง,สร้างใหม่ จากทรัพยากรที่มีอยู่
ผู้ที่ได้รับอนุญาตไม่สามารถถูกเพิกถอนเสรีภาพเหล่านี้ตราบใดที่คุณปฏิบัติตามข้อกำหนดสิทธิการใช้งาน

ภายใต้เงื่อนไขดังต่อไปนี้:

แสดงที่มา - คุณต้องให้เครดิตที่เหมาะสมเพื่อให้ลิงค์ไปยังใบอนุญาตและระบุว่ามีการเปลี่ยนแปลงหรือไม่
คุณสามารถทำได้ในลักษณะที่สมเหตุสมผล แต่ไม่ใช่ในลักษณะที่แนะนำผู้ให้อนุญาตให้การรับรองแก่คุณหรือการใช้งานของคุณ

ไม่ใช่เชิงพาณิชย์ - คุณไม่สามารถใช้ทรัพยากรเพื่อการค้าได้
'''

# clear screen 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

username = input('What is your name?\n')


# append data to student_data.json
def add_data():
  clear()
  name = input('What is Student name?\n')
  home_address = input('What is student home address?\n')
  gender = input('What is Student gender?\n')
  tel_num = int(input('What is Telephone number?\n'))
  email = input('What is student email?\n')

  currentTime = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
  information = {
    'name': name,
    'home_address': home_address,
    'gender': gender,
    'telephone': tel_num,
    'email': email,
    'added_by': username,
    'create_at': currentTime
  }

  get_json = get_data()

  if get_json == False:
    get_json = [information]
  else:
    get_json.append(information)

  file = open('student_data.json', 'w')
  file.write(json.dumps(get_json))
  file.close()
  
  clear()
  print('Data has been added!')
  time.sleep(1)
  clear()
  main_menu()

def get_data():
  try:
    file = open('student_data.json', 'r')
    data = file.read()
    return(json.loads(data))
  except:
    return(False)

# Show data from json
# 26/12/2019 i got this error "list indices must be integers or slices, not str"
# This problem has resolved by https://linuxconfig.org/how-to-parse-data-from-json-into-python

def show_data():
  clear()
  data = pathlib.Path('student_data.json')
  # i've fix "File not found" error message by using pathlib module 
  if data.exists():
      while True:
        with open('student_data.json', 'r') as info_read:
          info_data = json.load(info_read)
        clear()
        for data in info_data:
          print('==========================')
          print('Name: ' + data['name'])
          print('Address: ' + data['home_address'])
          print('Gender: ' + str(data['gender']))
          print('Tel: ' + str(data['telephone']))
          print('Generate on: ' + str(data['create_at']))
        print('')
        x = input('[0] Back to main menu\n')
        if x == '0':
            main_menu()
            break
        else:
            continue
  else:
      while True:
        clear()
        Data_ERR = input('ERR: File student_data.json not found.\nwould you like to add new data? [Y/N]\n')
        if 'Y' in Data_ERR or 'y' in Data_ERR:
          clear()
          add_data()
          break
        elif 'N' in Data_ERR or 'n' in Data_ERR:
          clear()
          main_menu()
          break
        else:
          continue
# That's all i know..


def admin_log():
  currentTime = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
  information = {
    'name': username,
    'create_at': currentTime
  }

  get_json = get_admin_data()

  if get_json == False:
    get_json = [information]
  else:
    get_json.append(information)

  file = open('admin_log.json', 'w')
  file.write(json.dumps(get_json))
  file.close()

def get_admin_data():
  try:
    file = open('admin_log.json', 'r')
    data = file.read()
    return(json.loads(data))
  except:
    return(False)

def show_admin_data():
    while True:
        clear()
        with open('admin_log.json', 'r') as info_read:
          info_data = json.load(info_read)  

        for data in info_data:
          print('==========================')
          print('Name: ' + data['name'])
          print('Login on: ' + str(data['create_at']))
        print('')

        x = input('[0] Back to main menu\n')
        if x == '0':
            main_menu()
            break
        else:
            continue

# remove student data only
def remove_data():
    while True:
        x = input('Are you sure [Y/N]?')
        if 'Y' in x or 'y' in x:
            check_data = pathlib.Path('student_data.json')
            if check_data.exists():
                clear()
                os.remove("student_data.json")
                print("File Removed!")
                time.sleep(1)
                main_menu()
                break
            else:
                clear()
                print("ERR: File student_data.json not found.")
                time.sleep(1)
                main_menu()
                break
            break
        elif 'N' in x or 'n' in x:
            clear()
            main_menu()
            break
        else:
            continue
       

# This is main menu content!
def main_menu():
    while True:
        clear()
        print('Welcome '+ username +datetime.now().strftime(" | %H:%M | %D |"))
        print('What do you want to do?')
        print('[1] Add Student data')
        print('[2] View Student data')
        print('[3] View Admin data')
        print('[4] Reset all student data')
        print('\n[0] Exit')
        x = int(input("Select your choice\n"))
        if x == 1:
            clear()
            add_data()
            break
        elif x == 2:
            clear()
            show_data()
            break
        elif x == 3:
            clear()
            show_admin_data()
            break
        elif x == 4:
            clear()
            remove_data()
            break
        elif x == 0:
            exit()
            break
        else:
            continue

if __name__ == "__main__":
    admin_log()
    main_menu()