from requests import get, post, delete, put

print(get('http://localhost:8000/api/v2/jobs/1').json())
# с id = 999 нет в базе
print(get('http://localhost:8000/api/v2/jobs/999').json())
# аргумент в виде строки
print(get('http://localhost:8000/api/v2/jobs/b'))

print(delete('http://localhost:8000/api/v2/jobs/1').json())
# с id = 999 нет в базе
print(delete('http://localhost:8000/api/v2/jobs/999').json())

print(get('http://localhost:8000/api/v2/jobs').json())

print(post('http://localhost:8000/api/v2/jobs', json={
    'team_leader': 'TEST JOB',
    'job': 'TEST JOB',
    'work_size': 'TEST JOB',
    'collaborators': 'TEST JOB',
    'start_date': 'TEST JOB',
    'end_date': 'TEST JOB',
    'category': 'TEST JOB',
    'is_finished': True
}))
# не хватает параметра
print(post('http://localhost:8000/api/v2/jobs', json={
    'team_leader': 'TEST JOB',
    'job': 'TEST JOB',
    'work_size': 'TEST JOB',
    'collaborators': 'TEST JOB',
    'start_date': 'TEST JOB',
    'end_date': 'TEST JOB',
    'category': 'TEST JOB'
}).json())
# пустой json
print(post('http://localhost:8000/api/v2/jobs', json={}).json())
