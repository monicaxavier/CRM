#Python-API


import requests

resp = requests.get('https://todolist.example.com/tasks/')
if resp.status_code != 200:
    raise ApiError('GET/tasks/{}'.format(resp.status_code))

for todo_item in resp.json():
    print todo_item
