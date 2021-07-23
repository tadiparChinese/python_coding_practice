from collections import defaultdict
d1 = {'a': 'test', 'b':'btest', 'd':'dreg'}
d2 = {'a': 'cool', 'b':'main', 'd':'clear'}

dd = defaultdict(list)
for d in (d1,d2):
    for key, value in d.items():
        dd[key].append(value)

print(dd)