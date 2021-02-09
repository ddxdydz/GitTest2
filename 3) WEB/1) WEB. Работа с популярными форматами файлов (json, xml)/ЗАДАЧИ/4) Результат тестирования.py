import json
from sys import stdin


verdicts = list(enumerate([elem.strip() for elem in stdin], 1))


with open('scoring.json', mode='r') as json_file:
    points = 0
    resp = json.loads(json_file.read())
    for num, verdict in verdicts:
        for res_dict in resp['scoring']:
            if num in res_dict['required_tests'] and verdict == 'ok':
                points += int(res_dict['points'] // len(res_dict['required_tests']))
                continue

print(points)


'''
ok
wa
ok
ok
wa
ok
wa
ok
'''
