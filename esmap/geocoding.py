import pandas as pd
import googlemaps

# initializing google maps
gkey = pd.read_csv("googleapi.csv")['key'].iloc[0]
gmaps = googlemaps.Client(key=gkey)

# read locations into a dataframe
df_nbhd = 0
#create new lat and long columns
# loop over the locations
    # for location in df['column with the strings']
    # add the coordinates to lat and long
#write the result to_excel()