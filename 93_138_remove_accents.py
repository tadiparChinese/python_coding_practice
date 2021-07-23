# removing accents from characters

import unidecode
 
str = 'Caf`e` Mu`nchen'
str = unidecode.unidecode(str)
print(str) # Cafe Munchen