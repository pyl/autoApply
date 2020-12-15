from bs4 import BeautifulSoup
import requests

url = "https://github.com/pittcsc/Summer2021-Internships"

source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')


#print(soup.prettify) contains no tables but print(soup.table) 
# works somehow 


print(soup.table.prettify())