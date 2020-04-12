import pandas as pd
import calendar as cd
import requests as rq

# Read cities.csv into a list

# Open file where the data will be stored
#f = open("im_es.csv", "a")

# IMPORTANT start from the inside of the loop
# Loop through cities list
    # Loop through AAAA-MM (from 2004-01-DD to 2020-03-DD)
        # For the GET request: use interval from 01 to lastday = cd.monthrange(2010, 1)[1]
        # Send GET request to site via requests
        # Read json string to a dataframe pd.read_json(contents)
        # Get value out of "Valor"
        # write to file a line as AAAA-MM-01,<Valor>\n