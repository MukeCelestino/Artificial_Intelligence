import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#  Using the data
df = pd.read_csv("https://gist.githubusercontent.com/tacksoo/3ba379df0f5249e3c64df14b77518486/raw/05e476b3a917b4e70f0f4a070b2686c28202e0ea/happy.csv")
# df.head()
plt.scatter(df.get("median_income"), df.get("happyScore"))

a, b = np.polyfit(df.get("median_income"), df.get("happyScore"),1) # y = a*x + b
print(a, b)

plt.plot(df.get("median_income"), a*df.get("median_income") + b)
plt.scatter(df.get("median_income"), df.get("happyScore"))

plt.show()

# According to the graph/plot, Happiness score increases as income increases
