# Distance converter from meter to km and km to meter

ops = input('km or m? ')
value = int(input('Value: '))

if ops == 'km':
  print(f'Meter:{value} * 1000 = {value * 1000}')

elif ops == 'm':
  print(f'KM: {value} / 1000 = {value / 1000}')

else:
  print("Can't convert!")


