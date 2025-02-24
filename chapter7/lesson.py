import re
# Optional matching with the question mark

# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())

# mo2 = batRegex.search('The Exploration of Batwoman')
# print(mo2.group())

# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
# print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, des, 1 partridge'))