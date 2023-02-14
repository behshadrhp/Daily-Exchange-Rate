import requests
from conf import URL


class DailyExchangeRate:

    def get_rate(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                return 'The operation was not successful. Please try again ...'
        except:
            return 'We encountered some problems while performing the operation. Please check your internet connection and try again'


if __name__ == '__main__':
    print(DailyExchangeRate.get_rate(URL))
