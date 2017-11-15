#!/usr/bin/env python

#preliminaries and BeutifulSoup code sources/references come from TA session notes, Assignment 5 "README", Class exercises, & https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import requests
from bs4 import BeautifulSoup as bs

## in case code is run independent of prior solution (e1.py)

election_ID = [] # empy list to be filled with years and election IDs
url_va = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
req  = requests.get(url_va)
html = req.content
soup = bs(html, 'html.parser')
tags = soup.find_all('tr', 'election_item')

election_dict = {}
for t in tags:
    year = t.td.text
    year_id = t['id'][-5:] #just want last 5 #s for ID
    election_ID.append(year + ' ' + year_id)
    election_dict[year] = year_id
#print(election_ID)




# Question 2:

base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
for year in election_dict.keys():
    addr = base.format(election_dict[year])
    with open( 'president_general_' + year + '.csv', 'w') as output:
        output.write(requests.get(addr).text) # write/save files for Presidential general election years
