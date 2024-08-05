import requests
from jsonschema import validate
from core.contracts import USER_DATA_SCHEME
import allure

BASE_URL = "https://reqres.in/"
LIST_USERS = "api/users?page=2"
EMAIL_ENDS = "@reqres.in"

@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение списка пользователей')
def test_list_users():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + LIST_USERS}'):
        response = requests.get(BASE_URL + LIST_USERS)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
        assert response.status_code == 200

    data = response.json()['data']
    for item in data:
        with allure.step('Проверем элемент из списка'):
            validate(item, USER_DATA_SCHEME)
            with allure.step('Проверяем окончание Email адреса'):
                assert item['email'].endswith(EMAIL_ENDS)
