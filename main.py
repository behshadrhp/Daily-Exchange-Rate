import requests
import json
import sys
from kavenegar import *
from conf import URL, RULES, API_KEY


class DailyExchangeRate:
    def get_rate(url):
        """
        send request for URL and get API Rate response 
        return : Convert json api response to data variable -> Dict oop python
        """

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

    def archive(base, date, rate):
        """
        get base, date, rate, save them to the archive dir
        return: rate.data
        """

        with open(f'archive/{base}-{date}.json', 'w') as file:
            file.write(json.dumps(rate))

    def send_message():
        """
        sand message for phone number
        """
        try:
            api = KavenegarAPI(API_KEY)
            params = {
                'sender': 'numbr-sender',
                'receptor': 'you-number-phone',
                'message': 'your-message'}
            response = api.sms_send(params)
            print(response)

        except APIException as e:
            print(e)
        except HTTPException as e:
            print(e)


if __name__ == '__main__':
    rate = DailyExchangeRate.get_rate(URL)

    if RULES['archive'] == True:
        archive = DailyExchangeRate.archive(
            rate['base'], rate['date'], rate['rates'])
    if RULES['send_message'] == True:
        DailyExchangeRate.send_message()
