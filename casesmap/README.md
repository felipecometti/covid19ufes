# Cases Map

Datasets used:

* Brasil<span>.io: [caso_full.csv](https://data.brasil.io/dataset/covid19/_meta/list.html)
* Kelvins' github: [municipios.csv](https://github.com/kelvins/Municipios-Brasileiros)

## Results

![](https://media.giphy.com/media/gKrx2mmH1WkTeIlRZt/giphy.gif)

## The process

The final product was made in three steps: generating the 2d histogram, treating
the output images in Photoshop and combining them in a video in Premiere Pro.

### The 2d histogram

Although it's rather bad at representing Earth (and definately at it's poles),
Mercator's projection has one big advantage: being cartesian. Making projecting
on them an effortless task.

So I found a background map for Brazil and plotted the histogram inside that map's
limits (in coordinates) using matplotlib. Finding this limit was sligtly tricky
as I had to overlay the background map on Google Earth Pro and adjust it until
I found a fit.

### The Adobe treatment

As the output of matplotlib is not a transparent layer, I had to edit that alpha
layer into it. Fortunately Photoshop has a batch processing function, so all I
had to do was set all up and wait.

After the histogram layers were all ready, I imported them to Premiere Pro and
added it over the background map that I found earlier.

And that was it basically. Maybe I could've done everything in python, but I kinda
doubt I could get the specific look I was going for.