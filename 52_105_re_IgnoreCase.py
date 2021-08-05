# In Python "re.IGNORECASE" flag can be added as a third parameter to the "match" or "search" method. (Regular Expression)

import re

str = ['Word', 'word', 'wORD', 'Hi']

for s in str:
    print('Testing '+ s + '...', end='')
    if  re.match('word', s, re.IGNORECASE):
        print('OK')
    else:
        print('Not OK')

# Testing Word...OK
# Testing word...OK
# Testing wORD...OK
# Testing Hi...Not OK