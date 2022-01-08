# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

url = 'https://eepublicdownloads.blob.core.windows.net/public-cdn-container/clean-documents/Publications/Statistics/MDV_data-2015-2019.xlsx'

url2 = 'https://transparency.entsoe.eu/transmission-domain/physicalFlow/show?name=&defaultValue=false&viewType=TABLE&areaType=BORDER_BZN&atch=false&dateTime.dateTime=06.01.2022+00:00|UTC|DAY&border.values=CTY|10Y1001A1001A83F!BZN_BZN|10YDOM-CZ-DE-SKK_BZN_BZN|10YPL-AREA-----S&dateTime.timezone=UTC&dateTime.timezone_input=UTC'

data = pd.read_excel(url)

b = data.count()

print(b)

dt=data.iloc[:,[1,2,3,7,9]]

df = dt[(dt.Country == 'FR')+(dt.Country == 'GB')+(dt.Country == 'DE')+(dt.Country == 'NL')]

print(df)

a = df.count()

print(a)

c = df['Country'].value_counts().head(30)

print(c)

pd.options.display.float_format = '{:,.0f}'.format

df.to_csv("EnergyTransition.csv")

sns.pairplot(df, hue="Country");




