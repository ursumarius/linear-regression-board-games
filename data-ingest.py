import csv
import requests
with requests.Session() as s:
    s.post(url, data=payload)
    download = s.get('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-01-25/details.csv')

