from bs4 import BeautifulSoup
import sys
import webbrowser
import requests
from lxml import html
url = "https://dgplug.org/irclogs/"
data = requests.get("https://dgplug.org/irclogs/" + sys.argv[1])
htmlData = BeautifulSoup(data.text, 'html.parser')
for link in htmlData.find_all('a'):
    link = link.get('href')
    string = str(sys.argv[1]) + "-" + str(sys.argv[2])
    if string in link:
        # webbrowser.open(url + sys.argv[1] + "/" + link)
        linkLists = requests.get(url + sys.argv[1] + "/" + link)
        for data in linkLists.content.split():
            head = "https://"
            data = str(data)
            if head in data:
                print(data) 
        # print(url + sys.argv[1] + "/" + link)
