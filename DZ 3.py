import pytest
import requests

apikey = "CbKl7EXw9vG2NG6zX3IjmZUsjXIbE4e3cUMQlXMy"
base_url = "https://api.nasa.gov/planetary/apod"
date = "2020-10-01"
url = f"{base_url}?api_key={apikey}&date={date}"

# Проверка ввода валидных данных (Ожидание: код ответа 200 и успешное выполнение запроса)
def test_valid_search():
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()['service_version'] == 'v1'

# Проверка, что ввод несуществующей даты вызывает код ответа 400 и сообщение о неправильном формате даты
def test_non_existant_date():
    date = "1800-32-34"
    url = f"{base_url}?api_key={apikey}&date={date}"
    response = requests.get(url)
    assert response.status_code == 400
    assert response.json()['msg'] == f"time data '{date}' does not match format '%Y-%m-%d'"

# Проверка валидных граничных значений даты (Ожидание: код ответа 200 и успешное выполнение запроса)
boundary_values = ("1995-06-16", "1995-06-17", "2024-02-09", "2024-02-10")
@pytest.mark.parametrize("value", boundary_values)
def test_date_boundary_values(value):
    date = value
    url = f"{base_url}?api_key={apikey}&date={date}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()['service_version'] == 'v1'

# Проверка невалидных граничных значений даты (Ожидание: код ответа 400 и сообщение об ошибке)
boundary_values = ("1995-06-15", "1800-06-17", "2024-02-11", "2030-02-10")
@pytest.mark.parametrize("value", boundary_values)
def test_date_invalid_boundary_values(value):
    date = value
    url = f"{base_url}?api_key={apikey}&date={date}"
    response = requests.get(url)
    assert response.status_code == 400
    assert response.json()['msg'] == 'Date must be between Jun 16, 1995 and Feb 10, 2024.'

# Проверка, что неправильный API KEY вызывает ошибку и код ответа 400 и больше
def test_invalid_apikey():
    apikey = "kukaracha"
    url = f"{base_url}?api_key={apikey}&date={date}"
    response = requests.get(url)
    assert response.status_code > 400
    assert response.json()['error']['code'] == 'API_KEY_INVALID'

# Проверка, что отсутствие API KEY вызывает ошибку и код ответа 400 и больше
def test_no_apikey():
    apikey = ""
    url = f"{base_url}?api_key={apikey}&date={date}"
    response = requests.get(url)
    assert response.status_code > 400
    assert response.json()['error']['code'] == 'API_KEY_MISSING'
