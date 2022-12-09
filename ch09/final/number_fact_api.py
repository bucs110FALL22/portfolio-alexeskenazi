import requests


class NumberFactApi:
    '''
    Proxy class around the public NumbersAPI to get a random fact about a number.
    See http://numbersapi.com/
    '''
    def __init__(self) -> None:
        '''
        Constructor
        '''
        self.api_url = 'http://numbersapi.com/{number}'

    def get(self, number: int) -> str:
        '''
        Gets a random fact about the input date.
        number: (int) a number to get a fact for
        return (str) fact about number.
        '''
        url = self.api_url.format(number=number)
        response = requests.get(url)
        return response.text if response else ''
