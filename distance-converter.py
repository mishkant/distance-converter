# Distance converter from meter to km and km to meter

ops = input('km or m? ')
value = int(input('Value: '))

if ops == 'km':
  print(f'Meter: {value * 1000}')

elif ops == 'm':
  pass

else:
  print("Can't convert!")


