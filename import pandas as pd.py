import pandas as pd
from pandas_profiling import ProfileReport
df=pd.read_csv("country_wise_latest.csv")
profile=ProfileReport(df)
profile.to_file(output_file="country.html")