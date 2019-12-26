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
  - Improve show_data() to beautiful look

'''


# append data to info.json
def keep_data():
  clear()
  name = input('\nWhat is Student name?\n')
  points = input('\nHow much points do student get?\n')

  #currentTime = int(datetime.timestamp(datetime.now()))
  currentTime = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
  information = {
    'name': name,
    'points': points,
    'added by': username,
    'create at': currentTime
  }

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
def show_data():
  
    with open('info.json') as myData:
      obj = json.loads(myData)
      for p in obj['name']:
        print('Name: ' + p['name'])


'''
  with open("info.json", "r") as info_read:
    data = json.load(info_read)
    print(data)
'''
# Clear data from json
def clear_data():
  clear()
  os.remove("info.json")
  print("File Removed!")

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