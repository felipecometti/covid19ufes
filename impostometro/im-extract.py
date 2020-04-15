import pandas as pd
import datetime as dt
import calendar as cd
import requests as rq
import time

# Read cities.csv into a list
city_df = pd.read_csv("cities.csv")
count_cities = len(city_df.index)
city_codes = city_df['Código'].tolist()
city_names = city_df['Município'].tolist()

# Open file where the data will be stored
f = open("im_es.csv", "a", encoding="utf8")
log = open("log.txt", "a")

log.write("==============================\n" + str(dt.datetime.now()) + "\n")
#count_cities = 3

# Loop through cities list
for x in range(0, count_cities):
    time_delta = dt.datetime.now()
    city = city_codes[x]
    city_name = city_names[x]
    # Loop through AAAA-MM (from 2004-01-DD to 2020-03-DD)
    for year in range(2004, 2021):
        for month in range(1, 13):
            # Get tax collection value from url dict
            url = "https://impostometro.com.br/Contador/Municipios"
            url = url + "?estado=es&municipio="
            url = url + str(city) + "&dataInicial="
            url = url + str(dt.date(year, month, 1).strftime("%d/%m/%Y")) + "&dataFinal="
            url = url + str(dt.date(year, month, cd.monthrange(year, month)[1]).strftime("%d/%m/%Y"))
            #getprs = {
            #    "estado": "es",
            #    "municipio": city,
            #    "dataInicial": dt.date(year, month, 1).strftime("%d/%m/%Y"),
            #    "dataFinal": dt.date(year, month, cd.monthrange(year, month)[1]).strftime("%d/%m/%Y")
            #}
            #contents = rq.get(url, params=getprs)
            contents = rq.get(url)
            contents = contents.text
            page_content = eval(contents)
            # write to file a line as AAAA-MM-01,<Valor>\n
            f.write(str(dt.date(year, month, 1).strftime("%d/%m/%Y")) + "," + \
            #f.write(str(getprs['dataInicial']) + "," + \
                city_name + "," + \
                str(page_content['Valor']) + "\n")
            print(str(x + 1) + "/" + str(count_cities), year, month, \
                end="               \r")
            if year == 2020 and month >= 3:
                break
    time_delta = dt.datetime.now() - time_delta
    log.write(str(x + 1) + "/" + str(count_cities) + " " + str(year) + \
        " " + str(month) + " " + str(time_delta) + "\n")
f.close()
log.write(str(dt.datetime.now()) + "\n" + "==============================\n")
log.close()
print("\nDone.")
input("Press enter to continue...")