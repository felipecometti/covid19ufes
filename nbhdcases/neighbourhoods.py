import pandas as pd

url = "https://coronavirus.es.gov.br/distribuicao-dos-casos-confirmados-da-covid-19-por-bairro"
df_list = pd.read_html(url)                     # Still getting used to pandas
df = df_list[-1]                                # Get last avaliable table
df.columns = df.iloc[0]                         # Define row 0 as headers
df = df.drop([0])                               # Drop row 0
df = df.dropna()                                # Drop NaNs

# Create date column (to be automated in the future)
get_date = input("Qual o dia de atualização (em ??/04/2020)? ")
get_date = get_date + "/04/2020"
df["Data"]=get_date

df.to_excel("CasosBairros.xlsx", sheet_name="Casos Bairros", index=False)