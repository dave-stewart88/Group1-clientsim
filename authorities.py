'''
Group 1
Luke Hamill (Main), Colm Mckeever, David Stewart, Kerry O'Hagen, Krishna Sreejesh
Created 08/03/2022
File for getting a list of the authorities for each eatery
'''
import json
import pandas as pd
import io
import os
import requests
from requests.structures import CaseInsensitiveDict


def main():
    auths = getAllAuthorities()
    auths.to_csv('./authorities/authorities-list.csv')
    urls = auths.FileName.values
    print(urls)
    for u in urls:
        filename = os.path.basename(u)
        base = os.path.splitext(filename)[0]
        filename = base + '.json'
        print(filename)

def getAllAuthorities():
    url = "https://api.ratings.food.gov.uk/Authorities"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "*/*"
    headers["x-api-version"] = "2"

    # load data using Python JSON module
    data = json.loads(requests.get(url, headers=headers).text)

    # Flattening JSON data
    df = pd.json_normalize(data, record_path=['authorities'])
    return df


if __name__ == "__main__":
    main()
