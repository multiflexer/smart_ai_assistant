import requests

def post_request(url, data):
    """
    Функция для отправки POST-запроса.

    :param url: URL-адрес для отправки запроса.
    :param data: Словарь, содержащий данные для отправки.
    :return: Ответ от сервера в формате JSON.
    """
    response = requests.post(url, json=data)
    return response.json()

def get_request(url, params=None):
    """
    Функция для отправки GET-запроса.

    :param url: URL-адрес для отправки запроса.
    :param params: Словарь, содержащий параметры запроса.
    :return: Ответ от сервера в формате JSON.
    """
    response = requests.get(url, params=params)
    return response.json()

def main():
    # Пример использования функций post_request и get_request
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"title": "foo", "body": "bar", "userId": 1}
    response = post_request(url, data)
    print(response)

    url = "https://jsonplaceholder.typicode.com/posts/1"
    params = {"userId": 1}
    response = get_request(url, params)
    print(response)

if __name__ == "__main__":
    main()
