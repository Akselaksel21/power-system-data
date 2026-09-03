# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:27:07 2026
@author: Aksel
"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("load/forbruk_2025.csv");
#Jeg får den til å lese tiden som tid og ikke tekst
df["Unnamed: 0"] = pd.to_datetime(df["Unnamed: 0"], utc=True)

#Jeg lager en gjennomsnitt for daten for måner basert på tiden. Jeg sortert
#listen etter Januar-desember for linje 20 sortere alfabetisk
monthly_avreage = df.groupby(df["Unnamed: 0"].dt.month)["Actual Load"].mean()
monthly_avreage.index = [
"Januar", "Februar", "Mars", "April",
"Mai", "Juni", "Juli", "August",
"September", "Oktober", "November", "Desember"
]
#Jeg lager variabler for min, max og std
monthly_std = df.groupby(df["Unnamed: 0"].dt.month)["Actual Load"].std()
monthly_std.index = [
"Januar", "Februar", "Mars", "April",
"Mai", "Juni", "Juli", "August",
"September", "Oktober", "November", "Desember"
]
monthly_Max = df.groupby(df["Unnamed: 0"].dt.month)["Actual Load"].max()
monthly_Max.index = [
"Januar", "Februar", "Mars", "April",
"Mai", "Juni", "Juli", "August",
"September", "Oktober", "November", "Desember"
]
monthly_Min = df.groupby(df["Unnamed: 0"].dt.month)["Actual Load"].min()
monthly_Min.index = [
"Januar", "Februar", "Mars", "April",
"Mai", "Juni", "Juli", "August",
"September", "Oktober", "November", "Desember"
]
#Jeg lager en liste med Min, max og std og gir vær en index navn.
statistikk_2025 = pd.DataFrame({
"Max": monthly_Max,
"Min": monthly_Min,
"Std": monthly_std
})
#Jeg lagrer resultaten for gjennomsnit, max, min og std i mape
statistikk_2025.to_csv("results/statistikk_2025.csv")
monthly_avreage.to_csv("results/manedlig_last_2025.csv")
#lager figur
plt.figure(figsize=(10, 5))
monthly_avreage.plot(kind="bar")
plt.title("Gjennomsnitt last i manen")
plt.savefig("results/manedlig_last_2025.png")
plt.show()
#Printer gjennomsnitt for måneder
print(monthly_avreage)
