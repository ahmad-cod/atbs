import random
numberOfStreaks = 0

for experimentNumber in range(10000):
  # Code that creates a list of 100 'heads' or 'tails' values.
  coin_flips = []
  for i in range(100):
    # Flip a coin and add the result to the list.
    
    coin_flips.append(random.choice(['H', 'T']))
    if coin_flips[-6:] == ['H']*6 or coin_flips[-6:] == ['T']*6:
      numberOfStreaks += 1
      break


  # Code that checks if there is a streak of 6 heads or tails in a row.
  print(coin_flips)
  print('Chance of streak: %s%%' % (numberOfStreaks / 100))