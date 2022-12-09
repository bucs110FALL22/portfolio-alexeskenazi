import requests


class AztroApi:
    '''
    Proxy class around the public Aztro to get horozcope info for a day.
    See https://aztro.readthedocs.io/en/latest/
    '''
    def __init__(self) -> None:
        '''
        Constructor
        '''
        self.api_url = 'https://aztro.sameerkumar.website/'
        self.signs = [
            'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
            'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
        ]

    def get_luck_of_the_day(self, lucky_number: int) -> str:
        '''
        Gets a string representing the "luck" assocaited with a given number 
        luck_number: (int) a number for which to get the luck of day.
        return: (str) a string containing the luck of the day.
        '''
        sign = self.convert_a_number_to_a_zodiac_sign(lucky_number)
        json = self.get_aztro_json(sign, 'today')
        return json['description']

    def get_aztro_json(self, sign: str, day: str):
        '''
        Gets today's luck for the input sign of the zodiac.
        sign: (str) one of these:  'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
            'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
        day: (str) on of these: 'yesterday', 'today', 'tomorrow'
        return: (Any) json containing the luck of the day for the input sign.
        '''
        response = self.get(sign, day)
        return response.json()

    def get(self, sign: str, day: str):
        '''
        Direct call to the API to get all the aztro info.
        sign: (str) one of these:  'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
            'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
        day: (str) on of these: 'yesterday', 'today', 'tomorrow'
        return: (Any) response containing the luck of the day for the input sign.
        '''
        params = (
                ('sign', sign),
                ('day', day),
                )
        return requests.post(self.api_url, params=params)

    def convert_a_number_to_a_zodiac_sign(self, lucky_number: int) -> str:
        '''
        Magically coverts any integer into a zodiac sign
        lucky_number: (int) number to convert.
        return: (str) zodiac sign
        '''
        return self.signs[(lucky_number % len(self.signs))]
