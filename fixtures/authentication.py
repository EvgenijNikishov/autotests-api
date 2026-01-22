
from pydantic import BaseModel, EmailStr
import pytest  # Импортируем pytest
# Импортируем API клиенты
from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.user.private_users_client import get_private_users_client, PrivateUsersClient
from clients.user.public_users_client import get_public_users_client, PublicUsersClient
from clients.user.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def authentication_client() -> AuthenticationClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с аутентификацией
    return get_authentication_client()

