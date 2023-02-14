import requests
import json
import sys
from conf import URL, RULES


class DailyExchangeRate:

    def get_rate(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data['success'] != True:
                    return 'The operation was not successful. Please try again ...'
                    sys.exit()
                return data
            else:
                return 'The operation was not successful. Please try again ...'
        except:
            return 'We encountered some problems while performing the operation. Please check your internet connection and try again'

    def archive(base, filename, rate):
        with open(f'archive/{base}-{filename}.json', 'w') as file:
            file.write(json.dumps(rate))


if __name__ == '__main__':
    rate = DailyExchangeRate.get_rate(URL)
    
    if RULES['archive'] == True:
        archive = DailyExchangeRate.archive(rate['base'], rate['date'], rate['rates'])
