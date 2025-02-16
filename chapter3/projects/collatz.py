def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result

while True:
  try:
      number = int(input('Enter an integer: '))
      break
  except ValueError:
      print('Please enter an integer.')
      

while number != 1:
    number = collatz(number)

