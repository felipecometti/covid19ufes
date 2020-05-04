import pandas as pd
import googlemaps
import json

# initializing google maps
gkey = pd.read_csv("googleapi.csv")['key'].iloc[0]
gmaps = googlemaps.Client(key=gkey)

# read neighbourhood names into a dataframe
df_nbhd = pd.read_csv("nbhd.csv")
total_nbhd = len(df_nbhd.index)

for x in range(0, total_nbhd):
    location = df_nbhd['MB'].iloc[x]
    print(x, location)
    request = gmaps.geocode(location)
    df_nbhd.loc[df_nbhd.index[x], 'latitude'] = request[0]['geometry']['location']['lat']
    df_nbhd.loc[df_nbhd.index[x], 'longitude'] = request[0]['geometry']['location']['lng']

df_nbhd.to_csv("nbhd.csv", index=False)