import requests
import json


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def create_user(self, email, password, name):
        """Создание пользователя через API"""
        url = f"{self.base_url}/auth/register"
        data = {"email": email, "password": password, "name": name}
        response = self.session.post(url, json=data)
        return response.json()

    def delete_user(self, access_token):
        """Удаление пользователя через API"""
        url = f"{self.base_url}/auth/user"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = self.session.delete(url, headers=headers)
        return response.status_code == 202

    def login(self, email, password):
        """Авторизация пользователя через API"""
        url = f"{self.base_url}/auth/login"
        data = {"email": email, "password": password}
        response = self.session.post(url, json=data)
        return response.json()

    def create_order(self, access_token, ingredients):
        """Создание заказа через API"""
        url = f"{self.base_url}/orders"
        headers = {"Authorization": f"Bearer {access_token}"}
        data = {"ingredients": ingredients}
        response = self.session.post(url, json=data, headers=headers)
        return response.json()

    def get_user_orders(self, access_token):
        """Получение заказов пользователя через API"""
        url = f"{self.base_url}/orders"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = self.session.get(url, headers=headers)
        return response.json()
