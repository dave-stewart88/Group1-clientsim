'''
Group 1
Luke Hamill (Main), Colm Mckeever, David Stewart, Kerry O'Hagen, Krishna Sreejesh
Created 08/03/2022
File for getting data from the Food Standards API and saving that data to a CSV for future work
'''
import json
import pandas as pd
import io
import os
import requests
from requests.structures import CaseInsensitiveDict


def main():
    auths = getAllBusinessNames()
    try:
        auths.to_csv('./food-hygiene-data/belfast-all.csv')
    except:
        print("File is already open elsewhere")

    businessNames = auths.BusinessName.values
    ratings= auths.RatingValue.values
    print(businessNames, ratings)


def getAllBusinessNames():
    url = "https://api.ratings.food.gov.uk/establishments?localAuthorityId=138"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "*/*"
    headers["x-api-version"] = "2"

    data = json.loads(requests.get(url, headers=headers).text)
    df = pd.json_normalize(data, record_path=['establishments'])
    return df


if __name__ == "__main__":
    main()
