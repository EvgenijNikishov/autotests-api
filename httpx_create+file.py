import httpx
import faker

#Создаем юзера
payload = {
    "email": faker.get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

response_create = httpx.post("http://localhost:8000/api/v1/users", json=payload)
responce_create_json = response_create.json()
user_id = responce_create_json["user"]["id"]
print(f"Успешно созданный пользователь: {responce_create_json}")

# Получаем токен
auth = {
  "email": responce_create_json["user"]["email"],
  "password": "string"
}

response_auth = httpx.post("http://localhost:8000/api/v1/authentication/login", json=auth)
response_auth_json = response_auth.json()
token = response_auth_json["token"]["accessToken"]
print(f"Получен токен авторизации: {token}")

create_file_header={
    "Authorization": f"Bearer {token}",
}

create_file_response = httpx.post(
    "http://localhost:8000/api/v1/files",
    data={"filename":"image.jpg","directory":"courses"},
    files={"upload_file":open("./testdata/files/image.jpg","rb")},
    headers=create_file_header
)
create_file_response_json = create_file_response.json()
print(create_file_response_json)