import requests
from conf import URL


def get_rate(url):
    response = requests.get(url)
    data = response.json()
    print(data)


if __name__ == '__main__':
    get_rate(URL)