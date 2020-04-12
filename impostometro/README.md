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