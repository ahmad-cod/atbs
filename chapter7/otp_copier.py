import pyperclip
import re

text = pyperclip.paste()

otpRegex = re.compile(' \d{4,6} ')

otpMatch = otpRegex.search(text).group()

pyperclip.copy(otpMatch)
print(otpMatch)