import requests
from conf import URL


class DailyExchangeRate:

    def get_rate(url):
        response = requests.get(url)
        data = response.json()
        print(data)


if __name__ == '__main__':
    DailyExchangeRate.get_rate(URL)
