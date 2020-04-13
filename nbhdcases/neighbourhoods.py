import pandas as pd

# Create date column (to be automated in the future)
get_date = input("Qual o dia de atualização (em ??/04/2020)? ")
get_date = get_date + "/04/2020"

# Load file to append, check if date is not already there
df_file = pd.read_excel("CasosBairros.xlsx")
if get_date not in df_file['Data'].tolist():
    # Get table from website
    url = "https://coronavirus.es.gov.br/distribuicao-dos-casos-confirmados-da-covid-19-por-bairro"
    df_list = pd.read_html(url)                     # Still getting used to pandas
    df = df_list[-1]                                # Get last avaliable table
    df.columns = df.iloc[0]                         # Define row 0 as headers
    df = df.drop([0])                               # Drop row 0
    df = df.dropna()                                # Drop NaNs
    df["Data"]=get_date

    df_file = df_file.append(df)
    df_file.to_excel("CasosBairros.xlsx", sheet_name="Casos Bairros", index=False)
else:
    print("A data já está na tabela.")