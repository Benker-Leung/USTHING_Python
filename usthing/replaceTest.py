import re


# time = ' \t\n      ab cde \t\n      '
time = '\r\n                        Various positions                    '


# replace \r\n

time = time.replace('\r\n', '')
time = time.replace('\n', '')
space = re.findall('\ {2,}', time)
for eachSpace in space:
    time = time.replace(eachSpace, '')

print(time)

















#
