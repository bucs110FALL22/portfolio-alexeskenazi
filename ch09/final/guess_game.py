import datetime
import date_fact_api
import number_fact_api
import aztro_api
import random

MAX_NUMBER_TO_GUESS = 100


class GuessName:
    def __init__(self) -> None:
        self.num_api = number_fact_api.NumberFactApi()

    def run(self):
        self.print_fun_fact_of_the_day()

        num_to_guess = random.randint(1, MAX_NUMBER_TO_GUESS)
        guessed = False
        stopped = False
        count = 0
        self.print_game_intro()
        while not guessed and not stopped:
            count += 1
            self.print_hint(num_to_guess, count)
            guess = input('What is your guess? ')
            if guess == str(num_to_guess):
                guessed = True
            elif guess[0] == 'q' or guess[0] == 'Q':
                stopped = True
            else:
                self.print_wrong_guess_info(num_to_guess, guess)
        
        if guessed:
            self.print_correclty_guessed_message(num_to_guess, count)
        else:
            self.print_user_quit_message(num_to_guess)

    def print_fun_fact_of_the_day(self):
        date_api = date_fact_api.DateFactApi()
        current_time = datetime.datetime.now()
        result = date_api.get(current_time.month, current_time.day)
        print('Welcome! Did you know that ' + result)

    def print_correclty_guessed_message(self, num_to_guess, count):
        print('Correct! You guessed it after ' + str(count) + ' tries!')
        aztro = aztro_api.AztroApi()
        ret = aztro.get_luck_of_the_day(num_to_guess)
        print('Here is your luck for today based on the number you guessed:')
        print('----------------------------------------------')
        print('"' + ret + '"')
        print('----------------------------------------------')

    def print_wrong_guess_info(self, num_to_guess, guess):
        if guess.isdigit():
            guess_int = int(guess)
            fact = self.num_api.get(guess_int)
            if guess_int > num_to_guess:
                print('Try a smaller number, ' + guess + ' is too big! ' + fact)
            else:
                print('Try a bigger number, ' + guess + ' is too small! by the way, did you know that ' + fact)
        else:
            print('Please enter a number of Q to quit.')

    def print_hint(self, num_to_guess, count):
        result = self.num_api.get(num_to_guess)
        hint = result.replace(str(num_to_guess), '')
        if count == 1:
            print('Here is your first hint:' + hint)
        else:
            print('New hint:' + hint)

    def print_game_intro(self):
        print('Guess what number between 1 and 100 I am thinking? (Enter your guess or Q to quit at any time)')

    def print_user_quit_message(self, num_to_guess):
        print('The number was ' + str(num_to_guess) + ', better luck next time!')
