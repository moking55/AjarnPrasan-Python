import json, os, time, os.path, pathlib
from datetime import datetime
from os import system, name, path

# clear screen function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

username = input('\nWhat is your name?\n')
clear()

'''
  ##### TODO ######

  - Add Grade Calculate func
  - Add login Log

'''

# append data to info.json
def keep_data():
  clear()
  name = input('What is Student name?\n')
  points = int(input('\nHow much points do student get?\n'))

  if points <= 100:
    #currentTime = int(datetime.timestamp(datetime.now()))
    currentTime = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    information = {
      'name': name,
      'points': points,
      'added by': username,
      'create at': currentTime
    }
  else:
    print('ERR: Do not enter values ​​greater than 100.')
    time.sleep(2)
    clear()
    landing()

  get_json = get_data()

  if get_json == False:
    get_json = [information]
  else:
    get_json.append(information)

  file = open('info.json', 'w')
  file.write(json.dumps(get_json))
  file.close()

  print('Data has been added!')
  time.sleep(1)
  clear()
  landing()

def get_data():
  try:
    file = open('info.json', 'r')
    data = file.read()
    return(json.loads(data))
  except:
    return(False)


# Show data from json
# 26/12/2019 i got this error "list indices must be integers or slices, not str"
# This problem has resolved by https://linuxconfig.org/how-to-parse-data-from-json-into-python
def show_data():
  clear()
  data = pathlib.Path('info.json')
  # i've fix "File not found" error message by using pathlib module 
  if data.exists():
    with open('info.json', 'r') as info_read:
      info_data = json.load(info_read)

    for data in info_data:
      print('==========================')
      print('Student: ' + data['name'])
      print('Points: ' + str(data['points']))
      print('Generate on: ' + str(data['create at']))
    print('')
  else:
      clear()
      Data_ERR = input('ERR: File info.json not found.\nwould you like to add new data? [Y/N]\n')
      while True:
        if 'Y' in Data_ERR or 'y' in Data_ERR:
          clear()
          keep_data()
          break
        elif 'N' in Data_ERR or 'n' in Data_ERR:
          clear()
          landing()
          break
        else:
          continue
# That's all i know..

  return_to_menu = input('[0] Return to main menu\n')
  while True:
    if return_to_menu == '0':
      clear()
      landing()
      break
    else:
      print('ERR: invalid number...')
      time.sleep(1)
      show_data()
      break

# This is a useless func ever but i've add it if you need that
'''
def check_data():
  file = pathlib.Path("info.json")
  if file.exists():
    clear()
    print ("Found info.json, Everything is fine.")
    time.sleep(2)
    clear()
  else:
    clear()
    Data_ERR = input('ERR: File info.json notfound\nwould you like to add new data? [Y/N]\n')
    while True:
      if 'Y' in Data_ERR or 'y' in Data_ERR:
        clear()
        keep_data()
        break
      elif 'N' in Data_ERR or 'n' in Data_ERR:
        clear()
        landing()
        break
      else:
        continue
'''


# Append activity_log to jsonfile
def login_log():
  log_time = datetime.now().strftime('%H:%M | %d/%m/%Y')
  log_data = {
    'username': username,
    'login_time': log_time
  }

  with open('Activity_log.json', 'w') as json_file:
    json.dump(log_data, json_file)


# show Acitivity log from json
def login_log_show():
  clear()
  with open('Activity_log.json', 'r') as info_data:
    log_data = json.load(info_data)

  for data in log_data:
    print('==[Activity]==============')
    print('Username: ' + log_data['username'])
    print('Login time: ' + str(log_data['login_time']))
    print('==========================')
    break
  print('')

  return_to_menu = input('[0] Return to main menu\n')
  while True:
    if return_to_menu == '0':
      clear()
      landing()
      break
    else:
      print('ERR: invalid number...')
      time.sleep(1)
      show_data()
      break

# Clear data from json
def clear_data():
  confirm = input('Are you sure? [Y/N]\n')
  while True:
    # IMPORTENT: if you want to make multiple chars check in input() you must type "'text' in *variable*" and type "or" and do it again!!!
    if 'Y' in confirm or 'y' in confirm:
      clear()
      os.remove("info.json")
      print("File Removed!")
      time.sleep(2)
      clear()
      landing()
      break
    elif 'N' in confirm or 'n' in confirm:
      clear()
      landing()
      break
    else:
      print('ERR: You must type Y or N only!')
      time.sleep(2)
      clear()
      landing()
      break

# Menu item
def landing():
  while True:
    print('Welcome ' + username + ' | ' + datetime.now().strftime('%H:%M | %d/%m/%Y'))
    print('What do you want to do?')
    print('[1] Add Student Data')
    print('[2] View Student Data')
    print('[3] View Activity Data')
    print('[4] Clear Data')
    print('\n[9] About this software')
    print('[0] Exit Program')
    x = int(input('Type number...\n'))
    if x == 1:
      keep_data()
      break
    elif x == 2:
      show_data()
      break
    elif x == 3:
      login_log_show()
      break
    elif x == 4:
      clear_data()
      break
    elif x == 9:
      clear()
      L_read = open('Licence', 'r')
      print(L_read.read())
      break
    elif x == 0:
      exit()
    else:
      clear()
      continue

if '__main__' == __name__:
  login_log()
  license_check = pathlib.Path('Licence')
  if license_check.exists():
    landing()
  else:
    print('ERR: Missing Licence File')
    exit()