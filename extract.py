# Your imports go here
import logging
import json
import re
logger = logging.getLogger(__name__)

'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''
def extract_amount(dirpath: str) -> float:

    logger.info('extract_amount called for dir %s', dirpath)
    path='/Users/devkaran/fyle-interview-de-intern'+dirpath[1:]+'/ocr.json'
    with open(path,'r') as rc:
            df=json.load(rc)
    l=[]
    for j in range(len(df['Blocks'])):
        try:
            l.append(df['Blocks'][j]['Text'])
        except:
            continue
    t=" ".join(l)
    t=re.sub(",","",t)
    t=re.findall(r'\d+\.\d+',t)
    amount=0.0
    expected_amount=0.0
    for item in t:
        amount=float(item)
        expected_amount=max(amount,expected_amount)
    return expected_amount
