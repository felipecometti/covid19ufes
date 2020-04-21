# Mapping Espirito Santo's Cases

## The Problem

We have a dataset with neighbourhoods' names and the number of cases in each,
but we can't plot it in a map without their geolocations because of limitations
in our map services (Tableau and my mapping script). They only work well down to
city level in the location hierarchy. Lower than that and we need the coordinates.

## The Solution - Coordinates

Google maps is generally better at recognizing location names, so as we have today
395 unique places, automating this process is very welcome.

We'll try to get as many geolocations as we can an use this on both our Tableau
dashboard and I'll use it in the second stage to plot a map similar to the one in
/casesmap/

## The Solution - Map

Mainly based on the process described on /casesmap/ I'll be running one using data
from the state of Espirito Santo.