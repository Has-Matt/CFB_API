import requests
from requests.exceptions import HTTPError
import pandas as pd
from pandas.io.json import json_normalize
import tkinter as tk

# TODO: Create user input field to define Year and Season Type
# Code to Normalize Output

year = '2019'
seasontype = 'Postseason'
url= 'https://api.collegefootballdata.com/games?year=' + year + '&seasonType=' + seasontype

response = requests.get(url)
# print(response.json())

df = json_normalize(response.json())

# print(df)

df.to_csv('.\CFB_Games.csv', header=True, index=False)

# df.to_csv('CFB_Games.csv')