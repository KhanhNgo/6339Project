"""
This folowing code was taken from https://gist.github.com/paulgb/5265767
Slight modifications were made. All credits are given to the original creator.

'''
Convert Yelp Academic Dataset from JSON to CSV

Requires Pandas (https://pypi.python.org/pypi/pandas)

By Paul Butler, No Rights Reserved
'''

"""

import json
import pandas as pd
from glob import glob

def convert(x):
    ob = json.loads(x)
    out = {}

    for k, v in ob.items():
        if isinstance(v, list):
            count = 0
            for item in v:
                count += 1
            out[k] = count
        elif isinstance(v, dict):
            count = 0
            for kk, vv in v.items():
                count += vv
            out[k] = count
        else:
            out[k] = v
               # del ob[k]

    return out



for json_filename in glob('*.json'):
    csv_filename = '%s.csv' % json_filename[:-5]
    print('Converting %s to %s' % (json_filename, csv_filename))
    df = pd.DataFrame([convert(line) for line in open(json_filename)])
    df.to_csv(csv_filename, encoding='utf-8', index=False)

