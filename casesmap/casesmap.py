import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

# Variables to mess with
the_bins = 200
the_cmap = "Reds" # "Reds" for light, "gist_heat" for dark

# Load caso_full.csv
cases = pd.read_csv("caso_full.csv", usecols=['city_ibge_code', 'date',\
    'last_available_confirmed', 'place_type'])
cases = cases[cases['place_type'] == "city"]

# Vmax
# Vmax as the maximum number of cases
#the_vmax = cases.loc[cases['last_available_confirmed'].idxmax()]
#the_vmax = the_vmax.last_available_confirmed
# Vmax as the average number of cases of the last date available
last_date = cases['date'].iloc[-1]
the_vmax = cases[cases['date'] == last_date]
the_vmax = the_vmax['last_available_confirmed'].mean()

# Load municipios.csv
cities = pd.read_csv("municipios.csv", usecols=['codigo_ibge', 'latitude', 'longitude'])

# Combine dfs by city_ibge_code | codigo_ibge
merged = pd.merge(cases, cities, how='left', left_on='city_ibge_code', right_on='codigo_ibge')
merged = merged.dropna()

# Create dates list
dates = merged['date'].drop_duplicates()
dates = dates.tolist()

for the_date in dates:
    print(the_date)
    to_plot = merged[merged['date'] == the_date]
    x = to_plot['longitude'].tolist()
    y = to_plot['latitude'].tolist()
    the_weights = to_plot['last_available_confirmed'].to_numpy()

    # Drawing map
    img = plt.figure(num=None, figsize=(20, 20), dpi=300, facecolor='w', edgecolor='w')
    plt.hist2d(x, y, bins=the_bins, norm=colors.PowerNorm(0.3, vmin=0, vmax=the_vmax),\
        cmap=the_cmap, weights=the_weights)
    plt.xlim(-75.2, -28.75)
    plt.ylim(-34.1, 5.6)
    if the_cmap == "Reds":
        plt.gca().set_facecolor('#FFF5F0')
    else:
        plt.gca().set_facecolor('#000000')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().axes.xaxis.set_visible(False)
    plt.gca().axes.yaxis.set_visible(False)
    plt.gca().axes.xaxis.set_ticklabels([])
    plt.gca().axes.yaxis.set_ticklabels([])
    img.add_subplot().text(-29.75, -33.1, the_date, fontsize=28, color='white', horizontalalignment='right')
    plt.savefig(the_date + '.png', bbox_inches=0)
    plt.close()