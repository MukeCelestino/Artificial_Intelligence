import matplotlib.pyplot as plt
import urllib.request
u = urllib.request.urlopen("https://gist.githubusercontent.com/tacksoo/32e5badc23f992b9dce6c8a65c456edf/raw/0105d13f86f5b5741d1efd00a382a43e3b5c8cd2/highpoints.csv")
data = u.read().decode('utf-8')
lines = data.split('\n')

states = []
heights = []

for line in lines:
  cols = line.split(",")
  states.append(cols[0])
  heights.append(int(cols[2]))

# print(states)
# print(heights)

# Bar graph for highest points of each US state
plt.figure(figsize=(18, 8))
plt.bar(states, heights, color='purple')
plt.xlabel('US States')
plt.ylabel('Height (feet)')
plt.title('Highest Points of Each US State')
plt.xticks(rotation=90, ha='center')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

# Plot lat and long
import pandas as pd
df = pd.read_csv("https://gist.githubusercontent.com/tacksoo/07ec0e01122d02f30ef02b3a8418391f/raw/a78acee82835ac9af0b8595651102f16362d0c62/states.csv")
df.head()
plt.scatter(df.longitude, df.latitude)

for x in range(len(df.longitude)):
  plt.annotate(df.name[x],(df.longitude[x],df.latitude[x]),ha="center")
plt.show()


# A different data set of Population in a village
# Sample data for population over ten years
years = list(range(2010, 2020))
population = [112233, 115678, 120056, 123678, 130000, 132567, 128000, 124500, 121000, 118000]

# Plotting the data
plt.plot(years, population, marker='o', linestyle='-')

# Adding the labels and title
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population of a Country Over Ten Years')

# Displaying the plot
plt.grid(True)
plt.show()