import time, sys

indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
  while True:
    print(' ' * indent, end='')
    print('********')
    time.sleep(0.1) # Sleep for 100 milliseconds.

    if indentIncreasing:
      # Increase the number of spaces:
      indent += 2
      if indent == 20:
        # Change direction:
        indentIncreasing = False

    else:
      # Decrease the number of spaces:
      indent -= 2
      if indent == 0:
        # Change direction:
        indentIncreasing = True

except KeyboardInterrupt:
  print(" Exiting... Goodbye!")
  sys.exit() # When Ctrl-C is pressed, end the program.
