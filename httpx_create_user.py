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

#Обновляем данные

payload_new = {
    "email": faker.get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

response_auth = httpx.patch(f"http://localhost:8000/api/v1/users/{user_id}", json=payload_new, headers={"Authorization": f"Bearer {token}" })
response_auth_json = response_auth.json()

print(response_auth.status_code)