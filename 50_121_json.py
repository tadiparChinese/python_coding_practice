# parsing json from a file

import json

#1.open the file
with open('test.json') as f:
    # 2. Parse JSON
    data = json.loads(f.read())

#what is the fourth letter?
print(data["letters"][3])