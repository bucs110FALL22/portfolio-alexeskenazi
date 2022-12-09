import requests


class TriviaAPI:

    def __init__(self, category=18, amount=1):
        self.url = f'https://opentdb.com/api.php?amount={amount}&category={category}'

    def get(self):
        r = requests.get(self.url)
        #response is just a json dictonary of values after .json() call
        response = r.json()
        #check to make sure I got a question, i.e. results
        if response.get('results'):
            return response['results']
        else:
            return None

    def change_category(self, category):
        pass
        #self.url = #...