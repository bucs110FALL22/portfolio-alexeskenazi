import requests


class NumbersAPI:

    def __init__(self, month, day):
        self.url = f'http://numbersapi.com/{month}/{day}/date'

    def get(self):
        r = requests.get(self.url)
        #response is just a json dictonary of values after .json() call
        response = r.json()
        #check to make sure I got a question, i.e. results
        print(response)
        if response.get('results'):
            return response['results']
        else:
            return None

    def change_category(self, category):
        pass
        #self.url = #...