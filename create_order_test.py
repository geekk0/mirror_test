import requests

url = "http://127.0.0.1:8000/orders"

payload = {
    'apartment_number': '111',
    'pet_name': 'Murzik',
    'pet_breed': 'Scottish',
    'walk_date': '02-03-2024',
    'walk_time': '16:00',
    'duration': 20
}
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, json=payload)

print(response.text)
