import os
import json
import emoji
from colorama import Fore

path = 'test-data-set'

total_receipts = 0
total_test_pass = 0

for dir in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir)):
        total_receipts = total_receipts + 1

        expected_file_path = os.path.join(path, dir, 'expected.json')
        with open(expected_file_path, 'r') as f:
            expected_amount = json.load(f)

        output_file_path = os.path.join(path, dir, 'output.json')
        with open(output_file_path, 'r') as f:
            output_amount = json.load(f)

        if expected_amount.get('amount') == output_amount.get('amount'):
            total_test_pass = total_test_pass + 1
            print(emoji.emojize(Fore.GREEN + os.path.join(path, dir) + ' --> Pass :thumbs_up:') + Fore.RESET)
        else:
            print(emoji.emojize(Fore.RED + os.path.join(path, dir) +  ' -->  Fail :thumbs_down:') + Fore.RESET )

    
print(Fore.CYAN + '\n\n\n* - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - ' + Fore.RESET)
if total_receipts == total_test_pass:
    print(Fore.GREEN + '100% test pass' + Fore.RESET)
else:
    print(Fore.RED + 'please try again ' + str(round(((total_test_pass/total_receipts)*100), 2)) + '% test passed' + Fore.RESET)
print(Fore.CYAN + '* - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - ' + Fore.RESET)