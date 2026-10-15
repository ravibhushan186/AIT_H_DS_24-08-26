'''
API: Application programming interface
DummyJSON (https://dummyjson.com/products) this link is for referance how data look like
'''

import json
from pprint import pprint

# data = '''{
# "Name": "Ravi Bhushan",
# "Age": 24,
# "Occupation": "Student"
# }
# '''

# convert = json.loads(data)
# print(type(convert))
# print(convert)

# json_string = json.dumps(convert)
# print(type(json_string))
# print(json_string)

# with open('student.json', 'r') as f:
#     data = json.load(f)
#     print(type(data))
#     # print(data)
#     # pprint(data)
#     pprint(data['students'][1]['name']) #To read the data name

med = None
with open('student.json', 'r') as f:
    data = json.load(f)
    med = data
    print(type(data))
    # print(data)
    # pprint(data)
    pprint(data['students'][1]['name']) #To read the data name

with open('stuclone.json', 'w') as f:
    info = json.dump(med,f, indent=4)