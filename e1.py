#!/usr/bin/env python

#preliminaries and BeutifulSoup code sources/references come from TA session notes, Assignment 5 "README", Class exercises, & https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import requests
from bs4 import BeautifulSoup as bs

election_ID = [] # empy list to be filled with years and election IDs
url_va = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
req  = requests.get(url_va)
html = req.content
soup = bs(html, 'html.parser')
tags = soup.find_all('tr', 'election_item')

election_dict = {}
for t in tags:
    year = t.td.text #get years
    year_id = t['id'][-5:] #get IDs
    election_ID.append(year + ' ' + year_id)
    election_dict[year] = year_id
print(election_ID) # solution set of years and corresponding election IDS
