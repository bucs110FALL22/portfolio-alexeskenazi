import requests


class DateFactApi:
    '''
    Proxy class around the public NumbersAPI to get a random fact about a date.
    See http://numbersapi.com/
    '''
    def __init__(self) -> None:
        '''
        Constructor
        '''
        self.api_url = 'http://numbersapi.com/{month}/{day}/date'

    def get(self, month: int, day: int) -> str:
        '''
        Gets a random fact about the input date.
        month: (int) 1 to 12 for the month.
        day: (int) 1 to 31 for the day. Overflows roll to the next month
        return (str) fact about the input date.
        '''
        url = self.api_url.format(month=month, day=day)
        response = requests.get(url)
        return response.text if response else ''
