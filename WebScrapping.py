# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", {"class": "wikitable"})

if table is None:
    raise Exception("Table not found — request likely blocked")

headers = [header.text.strip() for header in table.find_all("th")]
print(headers)

rows = table.find_all("tr")[1:]

data = []
for row in rows:
    cols = [col.text.strip() for col in row.find_all("td")]

    if len(cols) >= 6:
        rank = cols[0]
        name = cols[1]
        industry = cols[2]
        revenue = cols[3]
        revenue_growth = cols[4]
        headquarters = cols[5]

        data.append([rank, name, industry, revenue, revenue_growth, headquarters])

df = pd.DataFrame(data, columns=[
    "Rank", "Name", "Industry", "Revenue", "Revenue Growth", "Headquarters"
])

print(df.head())

df.to_csv("us_companies_by_revenue.csv", index=False)