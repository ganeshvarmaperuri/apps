from django.shortcuts import render

import pandas as pd
import PyPDF2
import tabula

file_path = "C:/Users/sai/Downloads/OpTransactionHistory11-11-2023 (1).xls"
csv_file_path = "C:/Users/sai/Downloads/output_csv_file.csv"

# df = pd.read_csv(csv_file_path, index_col="Unnamed: 1")

df = pd.read_excel(file_path, usecols="B,D,G:I")
df = df.dropna(subset=["Unnamed: 8"])
df.columns = df.iloc[0]
df = df[1:]

print(df)
