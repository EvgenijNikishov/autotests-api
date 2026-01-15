from clients.private_http_builder import AuthenticationUserDict
from clients.user.private_users_client import get_private_users_client
from clients.user.public_users_client import get_public_users_client, UserCreateRequestDict
from faker import get_random_email

public_users_client = get_public_users_client()

create_user_request = UserCreateRequestDict (
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)

client_user_response = public_users_client.create_user_api(create_user_request)
client_user_response_data = client_user_response.json()

authentication_user=AuthenticationUserDict (
    email=create_user_request["email"],
    password="string"
)

private_users_client = get_private_users_client(authentication_user)
client_user_response_data_get = private_users_client.get_user_me_api()
print(client_user_response_data_get.json())

