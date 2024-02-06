import requests
import json
from conftest import *

def test_post_bin(random_email, random_phone_number):
    global binId
    url = f"{BASE_URL}/api/bin"
    data = {
        "email": random_email,
        "phone": random_phone_number
    }
    response = requests.post(url=url, json=data)
    api_response_conditions(response)
    binId = response.json()["binId"]

def test_get_bin():
    global binId
    url = f"{BASE_URL}/api/bin/{binId}"
    response = requests.get(url=url)
    api_response_conditions(response)

def test_delete_bin():
    global binId
    url = f"{BASE_URL}/api/bin/{binId}"
    response = requests.delete(url=url)
    api_response_conditions(response)
