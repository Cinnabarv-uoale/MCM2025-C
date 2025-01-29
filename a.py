import pandas as pd

a = pd.read_csv("Data/summerOly_medal_counts.csv")

YearMedel = {}
YearMedelUSA = {}

for row in a.itertuples():
    if row.Year not in YearMedel:
        YearMedel[row.Year] = 0
        YearMedelUSA[row.Year] = 0
    
    if row.NOC == "United States":
        YearMedelUSA[row.Year]+=row.Total
    YearMedel[row.Year]+=row.Total

Yearl = YearMedelUSA.keys()
YearMedell = [YearMedel[year]for year in Yearl]
YearMedelUSAl = [YearMedelUSA[year] for year in Yearl ]
ratiol = [YearMedelUSA[year]/YearMedel[year] for year in Yearl if YearMedel[year] != 0]

df = pd.DataFrame({
    'Year': Yearl,
    'YearMedel': YearMedell,
    'YearMedelUSA': YearMedelUSAl,
    'ratio':ratiol
})

# 保存为 .csv 文件
df.to_csv('yearMedel.csv', index=False)