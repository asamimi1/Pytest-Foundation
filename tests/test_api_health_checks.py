import requests
from conftest import *

@pytest.mark.parametrize("domain", ["google", "yahoo", "youtube", "github"])
def test_get_health_checks(domain):
    url = f"http://www.{domain}.com"
    response = requests.get(url=url)
    api_response_conditions(response)