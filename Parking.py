from datetime import datetime
import json

costPerHour = 20 # money spend per hours

def main():
  calculate()

# if you want to change the 
def generate():
  jsonData = [
    {
      'name': 'John',
      'time': 1576320483, # time (fixed)
    },
    {
      'name': 'James',
      'time': 1576320235,
    },
  ]

  file = open('parkingLot.json', 'w')
  file.write(json.dumps(jsonData))
  file.close()
  
# Generate parkingLot.json for keep the data.
generate()

def calculate():
  file = open('parkingLot.json', 'r')
  jsonData = json.loads(file.read())
  file.close()

  name = input('What\'s your name: ')

  found = False
  parkAt = 0

  for key in jsonData:
    if key['name'] == name:
      parkAt = key['time']
      found = True
      break

  if found:
    checkout = int(datetime.timestamp(datetime.now()))
    totalTime = checkout - parkAt
    hours = int(totalTime / 60)
    total = round(hours * costPerHour, 2)
    print('Your parking for ' + str(hours) + ' hours or ' + str(totalTime) + ' minutes')
    print('Total cost is ' + str(total) + ' baht')
  else:
    print('Not found ' + name + '\'s data')

if __name__ == '__main__':
  main()
else:
  exit()