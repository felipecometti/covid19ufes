import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

df = pd.read_csv('nyc_taxi.csv', usecols=['dropoff_x', 'dropoff_y'])

x = df['dropoff_x'].tolist()
y = df['dropoff_y'].tolist()

plt.figure(num=None, figsize=(11, 8), dpi=300, facecolor='w', edgecolor='w')
plt.hist2d(x, y, bins=1000, norm=colors.PowerNorm(0.3), cmap='gist_heat')
plt.xlim(-80, -30)
plt.ylim(-36, 8)
plt.axis("off")
plt.savefig('output21.png', bbox_inches=0)