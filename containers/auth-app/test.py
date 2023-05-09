import requests


def test_get_token():
    url = "http://127.0.0.1:8080/api/v1/auth/token"
    data = {
        "username": "johndoe",
        "password": "secret",
    }

    response = requests.post(url, data=data)

    # You can print the status code and the response body as follows:
    print("Status code:", response.status_code)
    print("Response body:", response.text)
    print("Access Token:", response.json()["access_token"])
    access_token = response.json()["access_token"]
    return access_token


def test_get_user(access_token):
    url = "http://127.0.0.1:8080/api/v1/users"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(url, headers=headers)

    # You can print the status code and the response body as follows:
    print("Status code:", response.status_code)
    print("Response body:", response.text)


access_token = test_get_token()
test_get_user(access_token=access_token)
