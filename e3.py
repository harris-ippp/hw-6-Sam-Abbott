#!/usr/bin/env python

#preliminaries and BeutifulSoup code sources/references come from TA session notes, Assignment 5 "README", Class exercises, & https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
# %matplotlib inline # for Jupyter_NB

## in case code is run independent of prior solutions (e1.py & e2.py)


election_ID = [] # empy list to be filled with years and election IDs
url_va = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
req  = requests.get(url_va)
html = req.content
soup = bs(html, 'html.parser')
tags = soup.find_all('tr', 'election_item')

election_dict = {}
for t in tags:
    year = t.td.text
    year_id = t['id'][-5:]
    election_ID.append(year + ' ' + year_id)
    election_dict[year] = year_id
#print(election_ID)

### Question 3:


df_dict = {}
for year in election_dict.keys():
    header = pd.read_csv("president_general_" + year +  ".csv", nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv("president_general_" + year +  ".csv", skiprows = [1], index_col = 0, thousands = ",")
    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df = df[['Republican', 'Democratic', 'Total Votes Cast']]
    df["Year"] = int(year)
    df_dict[year] = df

#### Ran out of time and requisite understanding to complete this solution beyond the hint (TEARS & ANGER & SADNESS)!!!
