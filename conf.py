URL = 'https://api.exchangerate.host/latest'

API_KEY = "Your-API-KEY"

RULES = {
    'archive': True,
    'send_message': False,

    # preferred default is none
    'preferred_rates': ['IRR', 'IQD', 'USD', 'CAD', 'AED', 'BTC'],
}
