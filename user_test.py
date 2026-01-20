from api_client_get_user import create_user_request, get_user_response
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.user.private_users_client import get_private_users_client
from clients.user.public_users_client import get_public_users_client
from clients.user.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from faker import get_random_email
from tools.assertion.schema import validate_json_schema

public_user_create = get_public_users_client()

create_user_request = CreateUserRequestSchema (
    email= get_random_email(),
    password="String",
    last_name="String",
    first_name="String",
    middle_name="String"
)

create_user_response = public_user_create.create_user(create_user_request)

create_auth_token = AuthenticationUserSchema (
    email=create_user_request.email,
    password=create_user_request.password,
)

private_user_create = get_private_users_client(create_auth_token)
get_user_response=private_user_create.get_user_api(create_user_response.user.id)
get_user_responce_schema=GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.json(), schema=get_user_responce_schema)
