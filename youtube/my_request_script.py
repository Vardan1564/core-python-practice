import requests
from bs4 import BeautifulSoup
# aa obj url mate use thay che
url="https://www.youtube.com/watch?v=Nsb3bLIlO4w&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=89"

# ama url ma requests get karva mate thay che 
r= requests.get(url)

# ama text format ma karva name html  ma karva
soup=BeautifulSoup(r.text,"html.parser")
print(soup.prettify())