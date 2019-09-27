import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

url = "https://en.wikipedia.org/wiki/Demography_of_the_United_Kingdom"
table = pd.read_html(url,header=0)
table[17].set_index('Unnamed: 0', inplace=True)
table[17]['Average population[36]'] = table[17]['Average population[36]'].str.replace(" ","")
UK = table[17]
UK.index.names = ['Year']
UK.rename(columns={'Average population[36]' : 'UK'}, inplace=True)

url = "https://en.wikipedia.org/wiki/Demographics_of_France"
table = pd.read_html(url,header=0)
table[21]['Average population (1 January)'] = table[21]['Average population (1 January)'].str.replace(" ","")
France = table[21]['Average population (1 January)']

url = "https://en.wikipedia.org/wiki/Demographics_of_Germany"
table = pd.read_html(url,header=0)
table[5] = table[5].iloc[1:]
table[5]['Average population'] = table[5]['Average population'].str.replace(" ","")
Germany = table[5]['Average population']

url = "https://en.wikipedia.org/wiki/Demographics_of_Spain"
table = pd.read_html(url,header=0)
table[12] = table[12].iloc[:-1]
table[12]['Average population'] = table[12]['Average population'].str.replace(" ","")
Spain = table[12]['Average population']

url = "https://en.wikipedia.org/wiki/Demographics_of_Italy"
table = pd.read_html(url,header=0)
table[17]['Average population'] = table[17]['Average population'].str.replace(" ","")
table[17]['Average population'] = table[17]['Average population'].str.replace(",","")
Italy = table[17]['Average population']

eu_top_5 = UK.loc[:,['UK']]
eu_top_5['France'] = France.to_list()
eu_top_5['Germany'] = Germany.to_list()
eu_top_5['Spain'] = Spain.to_list()
eu_top_5['Italy'] = Italy.to_list()

eu_top_5 = eu_top_5.apply(pd.to_numeric)
eu_top_5 = eu_top_5/1000000

eu_top_5.plot()
plt.title("Population of the 5 largest economies in EU", fontsize=20,pad=30)
ax = plt.gca()
plt.xlabel("Year", fontsize=14)
plt.ylabel("Population in Millions", fontsize=14)
loc = plticker.MultipleLocator(base=10) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)
ax.axis([1900,2020,0,90])

start_of_WW1 = 1914
end_of_WW1 = 1918
great_depression = 1929
start_of_WW2 = 1939
end_of_WW2 = 1945
Berlin_wall_collapses = 1989
economical_crisis = 2008

plt.axvline(start_of_WW1, color="grey")
plt.axvline(end_of_WW1, color="grey")
plt.axvline(great_depression, color="black")
plt.axvline(start_of_WW2, color="grey")
plt.axvline(end_of_WW2, color="grey")
plt.axvline(Berlin_wall_collapses, color="black")
plt.axvline(economical_crisis, color="black")

plt.text(start_of_WW1+2, 93, "WW1", va='center', ha="center", bbox=dict(facecolor="w",alpha=0.5))
plt.text(great_depression, 93, 'great depression', va='center', ha="center", bbox=dict(facecolor="w",alpha=0.5))
plt.text(start_of_WW2+3, 93, 'WW2', va='center', ha="center", bbox=dict(facecolor="w",alpha=0.5))
plt.text(Berlin_wall_collapses, 93, 'Berlin wall collapses', va='center', ha="center", bbox=dict(facecolor="w",alpha=0.5))
plt.text(economical_crisis, 93, 'economical crisis', va='center', ha="center", bbox=dict(facecolor="w",alpha=0.5))

plt.show()