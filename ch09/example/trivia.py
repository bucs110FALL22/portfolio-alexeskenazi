#external library, much better than built in network library
import requests
#for shuffling possible answers later
import random 
import pprint

def trivia(category=18, amount=2):
    # know how to put together a URL
    # Know the URL of the API
    api_url = f'https://opentdb.com/api.php?amount={amount}&category={category}'
    #use requests library to get the data from the API
    #know how to use the requests lib
    response = requests.get(api_url)
    results = response.json() #APIs usually return json, so use .json() to convert
    #pprint.pprint(results)
    # understand the structure of the returned data
    for trivia in results['results']:
        pprint.pprint(trivia)
        #combine the incorrect and corrects into a single array
        correct_answer = [ trivia['correct_answer'] ]
        answers = trivia['incorrect_answers'] + correct_answer 
        #shuffle the array for random order
        random.shuffle(answers)
        
        print(f"{trivia['question']} \n-- Please select the correct answer:\n===")
        
        #enumerate(): returns a tuple of the index and the value for each list item
        #display all possible answers
        for i, a in enumerate(answers):
            print(f"{i}){a}")

        #ask the user for their choice
        choice = int(input(":"))
        if answers[choice] == trivia['correct_answer']:
            print("correct, I guess.")
        else:
            print(f"Actually, {trivia['correct_answer']}")