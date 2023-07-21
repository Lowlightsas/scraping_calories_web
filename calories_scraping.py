from bs4 import BeautifulSoup
import requests
import json
url = "https://health-diet.ru/table_calorie/"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}
req = requests.get(url,headers=headers)
src = req.text
soap = BeautifulSoup(src,'lxml')
with open('index.html','w',encoding='utf-8') as file:
    file.write(src)

all_categories_dict = {}
all_product = soap.find_all(class_="mzr-tc-group-item-href")
for item in all_product:
    item_text = item.text
    item_href = 'https://health-diet.ru' + item.get('href')
    all_categories_dict[item_text] = item_href

with open('all_categories_dictt.json','w') as file:
    json.dump(all_categories_dict,file,indent=4,ensure_ascii = False)

