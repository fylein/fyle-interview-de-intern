# Your imports go here
import logging

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
    # your logic goes here
     ocr_file =os.path.join(dirpath,'ocr.json')
    text_data = []
    amt = 0.0
    act_amt = 0.0
    with open(ocr_file, mode='r', encoding="utf-8") as f:
        data = (json.load(f)).get("Blocks")

    for i in  data:
        try:
            text_data.append(i['Text'].upper()) 
        except KeyError:
            continue


    
    for dt in text_data:
        if "," in dt:
            dt = dt.replace(",",'')

        
        value =os.read.findall(r"[+-]?\d+\.\d+", dt)
        if len(value) > 0:
            amt = float(value[0])
            act_amt = max(act_amt,amt)
    return act_amt

    return 0.0

print(extract_amount("data\receipt19\expected.json"))

    return 0.0
