import requests
from io import StringIO
import pandas as pd

url = 'https://raw.githubusercontent.com/lorey/list-of-countries/refs/heads/master/csv/countries.csv'
req = requests.get(url)
data = StringIO(req.text)
print(pd.read_csv(data, sep = ';', on_bad_lines='skip'))