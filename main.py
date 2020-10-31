import requests
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

# Load webpage content
r = requests.get(
    "https://www.jumia.co.ke/43a7100f-43-4k-framless-hdr-ultra-uhd-smart-tv-model-2020-hisense-mpg258296.html",
    headers=headers)

# Convert to BS object
soup = bs(r.content, 'html.parser')

span = soup.find("span", attrs={'class': '-fs24'}).get_text()
price = span[4:]
string_price = str(price).replace(',', '')
final_price = float(string_price)

if final_price < 30000:
    print('You can now buy')
else:
    print('Price still high')
