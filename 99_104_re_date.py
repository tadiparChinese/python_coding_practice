# To extract more than one piece from a string using regular expressions, use captures

import re

date = '2021-06-09'
match = re.search('(\d+)-(\d+)-(\d+)', date)

if match:
    print(match.groups())
    # this is a tuple
    print(type(match.groups())) #('2021', '06', '09') #<class 'tuple'>