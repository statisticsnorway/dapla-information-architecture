import pandas as pd

csv_file = r'C:\BNJ\prosjektutvikling\GitHub\statisticsnorway\dapla-information-architecture\example_dataset\befolkningsdata\befolkningsdata.csv'

df = pd.read_csv(csv_file, sep=';', header=None, dtype={0:'string', 1:'string', 2:'string', 3:'int'}, infer_datetime_format=True, parse_dates=[4] )
header_columns = ["fnr", "bostedskommune", "sivilstand", "skattepliktig_formue", "dato"]
df.columns = header_columns

#print(df.to_string())
print(df)
print(df.dtypes)

parquet_file = csv_file.replace(".csv", ".parquet")
print(parquet_file)

df.to_parquet(parquet_file)
