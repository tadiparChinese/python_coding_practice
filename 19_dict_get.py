# safer way of reading values from a dictionary

data = {
    'Frace' : 'Paris',
    'Italy' : 'Rome'
}
# capital  = data['Germany'] # error

capital = data.get('Germany') #ok
#but it returns "None"
print(capital)

capital = data.get('Germany', '??')
print(capital) # prints "??"