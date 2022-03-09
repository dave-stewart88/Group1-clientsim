import csv
import json
import pandas as pd
import io
import os
import requests
from pandas import DataFrame
from requests.structures import CaseInsensitiveDict
def main():
  f = "./food-hygiene-data/belfast-all.csv"
  d = pd.read_csv(f,header=0,index_col=["BusinessName"],usecols=["BusinessName","RatingValue"])
  print(d.to_string())
  return d.to_string()

if __name__ == "__main__":
  main()