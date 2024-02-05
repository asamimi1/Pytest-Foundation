import pytest
import random
import string
from config import *

@pytest.fixture
def random_email():
    characters = string.ascii_letters + string.digits
    random_value = ''.join(random.choice(characters) for _ in range(8))
    email = f"test+{random_value}@email.com"
    return email

@pytest.fixture
def random_phone_number():
    valid_digits = "0123456789"
    random_digits = "".join(random.choice(valid_digits) for _ in range(9))
    phone_number = f"1{random_digits}"
    return phone_number

def api_response_conditions(response):
    allowed_status_codes = [200, 201, 202, 203, 204, 205]
    try:
        assert response.status_code in allowed_status_codes, f"API Response Status Code: {response.status_code}"
    except:
        raise