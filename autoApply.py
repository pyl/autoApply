from bs4 import BeautifulSoup
import requests
import pprint
from collections import OrderedDict

url = "https://github.com/pittcsc/Summer2021-Internships"

source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

table = soup.table
#print(soup.prettify) contains no tables but print(soup.table) 
# works somehow 
rows = table.find_all('tr')
rows.pop(0)

links = []

linkdict = OrderedDict()
for x in rows:
    if x.td.a is not None:
        try:
            linkdict[x.td.a.text] = x.td.a.get('href')
        except:
            print("ERROR" + x.td.a)
    else:
        linkdict[x.td.text] = None

collections.OrderedDict(reversed(list(tempdict.items())))
pprint.pprint(linkdict)