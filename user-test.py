from api_client_get_user import public_users_client
from clients.user.public_users_client import get_public_users_client
from clients.user.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from faker import get_random_email
from jsonschema import validate

public_users_client = get_public_users_client()


create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",  # Передаем аргументы в формате snake_case вместо camelCase
    first_name="string",  # Передаем аргументы в формате snake_case вместо camelCase
    middle_name="string"  # Передаем аргументы в формате snake_case вместо camelCase
)

create_user_response = public_users_client.create_user_api(create_user_request)

create_user_response_schema = CreateUserResponseSchema.model_json_schema()

validate(instance=create_user_response.json(),schema=create_user_response_schema)