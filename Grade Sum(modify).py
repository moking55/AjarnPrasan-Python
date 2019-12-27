import json, os, time
from datetime import datetime
from os import system, name

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
print('\nWelcome ' + username)


'''
  ##### TODO ######

  - Add Grade Calculate func

'''

# append data to info.json
def keep_data():
  clear()
  name = input('\nWhat is Student name?\n')
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
  clear()
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
  with open('info.json', 'r') as info_read:
    info_data = json.load(info_read)

  for data in info_data:
    print('==========================')
    print('Student: ' + data['name'])
    print('Points: ' + str(data['points']))
    print('Generate on: ' + str(data['create at']))
  print('')
# That's all i know..

  after = input('[0] Return to main menu\n')
  while True:
    if after == '0':
      clear()
      landing()
    else:
      continue

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
    elif 'N' in confirm or 'n' in confirm:
      clear()
      landing()
    else:
      print('ERR: You must type Y or N only!')
      time.sleep(2)
      clear()
      landing()


# Menu item
def landing():
  while True:
    print('\nWhat do you want to do?')
    print('[1] Add Student Data')
    print('[2] Check Student Data')
    print('[3] Clear Data')
    print('[4] Exit Program')
    x = int(input('Type number...\n'))
    if x == 1:
      keep_data()
      break
    elif x == 2:
      show_data()
      break
    elif x == 3:
      clear_data()
      break
    elif x == 4:
      exit()
    else:
      continue

if '__main__' == __name__:
  landing()