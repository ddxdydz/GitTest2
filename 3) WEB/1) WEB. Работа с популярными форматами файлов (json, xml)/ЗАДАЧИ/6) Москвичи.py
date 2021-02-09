import json
from zipfile import ZipFile


zip_name = 'input.zip'
with ZipFile(zip_name) as myzip:
    res_num = 0
    for obj_name in myzip.namelist():
        if '.json' in obj_name:
            resp = json.loads(myzip.read(obj_name))
            if resp['city'] == 'Москва':
                res_num += 1
print(res_num)
