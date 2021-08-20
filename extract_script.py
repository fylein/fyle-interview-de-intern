from colorama import Fore
import sys
import os
import json
import time

# your import goes here
import re

'''
    handle_error function helps to raise errors when and where needed
'''
def handle_error():
    print(Fore.RED + '\n\n Please specify valid path for which you want to run the test \n\n' + Fore.RESET)
    sys.exit()


'''
    validate_path
    input:
        - path: source of the receipts or raw data
    
    validate_path function takes in path as an input and return boolean after validating path
'''
def validate_path(path):
    try:
        if not os.path.exists(path):
            raise ValueError()
        else:
            return True

    except (IndexError, ValueError):
        handle_error()


'''
    extract_amount
    input:
        - path: source of the receipts or raw data
    
    output:
        - returns the extracted amount

'''
def extract_amount(path):
    # remove below line while implementing
    raise NotImplementedError
    
    # your logic goes here


'''
    main:
    entry point of the program

    iterates through given path
    writes output data into output.json 
'''
def main(path):
    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir)):
            extracted_amount = extract_amount(os.path.join(path, dir))

            data = {
                'amount': extracted_amount
            }

            with open(os.path.join(os.path.join(path, dir), 'output.json'), 'w') as f:
                json.dump(data, f, indent=4)

    # uncomment below lines when read to showoff
    # print(Fore.YELLOW + '\n\n hold on, running test set for you')
    # time.sleep(2)
    # os.system('python backtest.py')

if __name__ == '__main__':
    path = sys.argv[1]

    if validate_path(path):
        main(path)
    else:
        handle_error()