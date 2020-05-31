import re

with open('shaghai_if_config_test.txt', 'r') as fh:
     for line in fh.readlines():
         number_match = re.match('([+-]?([0-9]*[,])?[0-9]+)',line)
         namelookup_match = re.match('^time_namelookup:', line)
         print(number_match)
         if namelookup_match and number_match:
             num = number_match.group(0)
             print(num)
             continue
