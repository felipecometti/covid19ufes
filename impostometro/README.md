# Impostometro

Impostometro.com.br is a brazilian website designed as a way to criticize the
amount of taxes that are paid by the population. For that, they display on their
website (and sometimes using phisical LED bords) an estimation of how much
brazilians have paid for the government on direct and indirect taxation.

## Motivation

COVID-19 is surely impacting our state economy, but we mostly don't know by how
much. So a good way to quantify it is to analyze how much has tax collection
decreased over that time of pandemic.

## As brazilians say: "the cat's jump"

Impostometro's website also have some tools on their website to display historical
data, but unfortunately they don't allow us to export that data.

Or do they?

Well, turns out the javascript object that calls the historical value does this
using a (*snaredrums*) GET request! With state, city, start_date and end_date
variables! This GET request returns a json-like object.

So we seem to have everything set to get over those obstacles.

### Tools I'll be using

* Python 3.7
* Pandas lib
* Requests lib
* Simple file manipulation

## Findings

So I've found an issue with requests' get() function when passing the parameters
as a variable, as in 'rq.get(url, params='list')'. Requests becomes really slow
for some reason. It was taking a lot of time, so I ended up just building the
url as a string and sending it directly to 'rq.get(url)'.

It went from 21s/request to 0.5s/request.

The problem is probably in parsing those parameters. I tried to look into the
source for Requests a little but everything seemed normal.

Well, such is life with it's misteries. Point is that it's better to use string
operations to build the url if you want to make a lot of GET requests.

# Impostometro Stage 2

## Goal

It's simple, just need to correct the values for inflation.

### Tools

* Slightly more complex file manipulation
* Maybe I'll test pandas' performance, the 'im-extract.py' output has 15k lines