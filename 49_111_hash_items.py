#iterating over the dictionary items

capitals = {
    'France':'Paris',
    'Germany':'Berlin'
}

for country, city in capitals.items():
    print(f'The Capital of {country} is {city}')
