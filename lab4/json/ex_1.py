# Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.

import json
from data import datik

array = [["DN", "Description", "Speed", "MTU"], ['-' * 50, '-' * 20, '-' * 10, '-' * 10]]
print('Interface Status')
print('=' * 100)

superdatik = dict(json.loads(datik))
for value in superdatik["imdata"]:
    arruy = []
    dictik = value["l1PhysIf"]["attributes"]

    arruy.append(dictik["dn"])
    arruy.append(dictik["descr"])
    arruy.append(dictik["speed"])
    arruy.append(dictik["mtu"])

    array.append(arruy)

for i in array:
    num = 0
    for j in i:
        print(j, ' ' * (len(array[1][num]) - len(j)), end=' ')
        num += 1
    print()