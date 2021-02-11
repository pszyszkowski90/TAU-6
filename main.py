import requests
import json

url = "https://crudcrud.com/api/dcfbb8d30aac4e9bb4201ca3f1935ecc/unicorns"
data = {"name": "Sparkle Angel", "age": 2, "colour": "blue"}
data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}

# Test 1 POST
response = requests.post(url, data=data_json, headers=headers)
a = json.loads(response.text)
expected = ['name', 'age', 'colour', '_id']
current = []
for key, value in a.items():
    if key in expected:
        current.append(key)
assert expected == current
assert response.status_code == 201

# Test 2 GET
response = requests.get(url, data=data_json, headers=headers)
a = json.loads(response.text)
assert response.status_code == 200
assert len(a) > 0

# Test 3 PUT
data = {"name": "XXX", "age": 2, "colour": "blue"}
data_json = json.dumps(data)
response = requests.put(url + '/' + a[0].get('_id'), data=data_json, headers=headers)
assert response.status_code == 200

# Test 4 GET
response = requests.get(url + '/' + a[0].get('_id'), headers=headers)
a = json.loads(response.text)
assert a.get('name') == 'XXX'

# Test 5 DELETE
response = requests.delete(url + '/' + a.get('_id'), headers=headers)
assert response.ok == True

# Test 6 GET
response = requests.get(url + '/' + a.get('_id'), headers=headers)
assert response.status_code == 404
assert response.ok == False
