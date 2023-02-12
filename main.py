import requests
from conf import URL


def get_rate(url):
    response = requests.get(url)
    print(response.status_code)


if __name__ == '__main__':
    get_rate(URL)