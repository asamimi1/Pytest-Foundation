import requests
import json
from conftest import *

# Standard Tests

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

    data = response.json()
    print(data)

def test_get_bin():
    global binId
    url = f"{BASE_URL}/api/bin/{binId}"
    response = requests.get(url=url)
    api_response_conditions(response)

    data = response.json()
    print(data)

def test_delete_bin():
    global binId
    url = f"{BASE_URL}/api/bin/{binId}"
    response = requests.delete(url=url)
    api_response_conditions(response)

    data = response.json()
    print(data)

# Alternative Tests

def test_post_bin2(random_email, random_phone_number):
    data = {
        "email": random_email,
        "phone": random_phone_number
    }

    # Create Bin
    create_bin_response = create_bin(data)
    api_response_conditions(create_bin_response)
    binId = create_bin_response.json()["binId"]

    data = create_bin_response.json()
    print(data)

    # Get Bin
    get_bin_response = get_bin(binId)
    api_response_conditions(get_bin_response)

    data = create_bin_response.json()
    print(data)

    # Delete Bin
    delete_bin_response = delete_bin(binId)
    api_response_conditions(delete_bin_response)

    data = create_bin_response.json()
    print(data)

def create_bin(data):
    url = f"{BASE_URL}/api/bin"
    return requests.post(url=url, json=data)

def get_bin(binId):
    url = f"{BASE_URL}/api/bin/{binId}"
    return requests.get(url=url)

def delete_bin(binId):
    url = f"{BASE_URL}/api/bin/{binId}"
    return requests.delete(url=url)
