# iteration over dictionary

data = {
    'France':'Paris',
    'Germany':'Berlin',
    'Italy':'Rome',
    'India':'New Delhi'
}

# for country in data:
#     print('The capital of ' + country + ' is ' + data[country])

for country, capital in data.items():
    print(f'the capical of {country} is {capital}')