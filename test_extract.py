import os
import json
import pytest
import logging
from extract import extract_amount

logger = logging.getLogger(__name__)

# path = 'data'

# total_receipts = 0
# total_test_pass = 0

# for dir in os.listdir(path):
#     if os.path.isdir(os.path.join(path, dir)):
#         total_receipts = total_receipts + 1

#         expected_file_path = os.path.join(path, dir, 'expected.json')
#         with open(expected_file_path, 'r') as f:
#             expected_amount = json.load(f)

#         output_file_path = os.path.join(path, dir, 'output.json')
#         with open(output_file_path, 'r') as f:
#             output_amount = json.load(f)

#         if expected_amount.get('amount') == output_amount.get('amount'):
#             total_test_pass = total_test_pass + 1
#             print(emoji.emojize(Fore.GREEN + os.path.join(path, dir) + ' --> Pass :thumbs_up:') + Fore.RESET)
#         else:
#             print(emoji.emojize(Fore.RED + os.path.join(path, dir) +  ' -->  Fail :thumbs_down:') + Fore.RESET )

    
# print(Fore.CYAN + '\n\n\n* - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - ' + Fore.RESET)
# if total_receipts == total_test_pass:
#     print(Fore.GREEN + '100% test pass' + Fore.RESET)
# else:
#     print(Fore.RED + 'please try again ' + str(round(((total_test_pass/total_receipts)*100), 2)) + '% test passed' + Fore.RESET)
# print(Fore.CYAN + '* - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - ' + Fore.RESET)



def get_test_dirpaths():
    dirpaths = []
    for dir in os.listdir('./data'):
        dirpaths.append(os.path.join('./data', dir))
    return dirpaths


dirpaths = get_test_dirpaths()

@pytest.mark.parametrize('dirpath', dirpaths)
def test_extract(dirpath):
    expected_filepath = os.path.join(dirpath, 'expected.json')
    with open(expected_filepath, 'r') as f:
        expected_amount = json.load(f).get('amount')
    extracted_amount = extract_amount(dirpath)
    assert expected_amount == extracted_amount, 'Expected and extracted amounts do not match'