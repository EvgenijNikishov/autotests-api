from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.public_http_builder import get_public_http_client


class UserCreateRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    def create_user_api (self,request:UserCreateRequestDict) -> Response:
        """
        Выполняет POST-запрос.

        :param email: email пользователя.
        :param password: password пользователя.
        :param lastName: lastName пользователя.
        :param firstName: firstName пользователя.
        :param middleName: middleName пользователя.
        :return: Объект Response с данными ответа.
        """
        return self.post("/api/v1/users/create", json=request)

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())