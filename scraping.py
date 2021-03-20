import requests
import json
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
r = requests.get(url)

soup = BeautifulSoup(r.content,'html5lib')
tags = []
final = {}
final1 = []
quote = soup.findAll('div',attrs={'class':'quote'})
for row in quote:
    quo = row.find('span',attrs={'class':'text'}).text
    author = row.find('small',attrs={'class':'author'}).text
    for row1 in row.findAll('a',attrs={'class':'tag'}):
        tags.append(row1.text)
    final['quote']=quo
    final['author']=author
    final['tags']=tags
    tags = []
    final1.append(final)
disc = {"quotes":final1}
js = json.dumps(disc,indent=3)
print(js)

with open(r"C:\Users\Vaibhav\Desktop\Python Workshop\quotes.json","w") as out:
    json.dump(disc,out)

    