
from pydantic import BaseModel, EmailStr
import pytest  # Импортируем pytest
# Импортируем API клиенты

from clients.private_http_builder import AuthenticationUserSchema
from clients.user.private_users_client import get_private_users_client, PrivateUsersClient
from clients.user.public_users_client import get_public_users_client, PublicUsersClient
from clients.user.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:  # Быстрый доступ к email пользователя
        return self.request.email

    @property
    def password(self) -> str:  # Быстрый доступ к password пользователя
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email, password=self.password)




@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def public_users_client() -> PublicUsersClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с публичным API пользователей
    return get_public_users_client()

@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def private_users_client(function_user:UserFixture) -> PrivateUsersClient:  # Аннотируем возвращаемое фикстурой значение
    return get_private_users_client(function_user.authentication_user)

@pytest.fixture
# Используем фикстуру public_users_client, которая создает нужный API клиент
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)  # Возвращаем все нужные данные