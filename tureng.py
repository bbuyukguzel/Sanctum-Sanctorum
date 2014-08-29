from bs4 import BeautifulSoup
import requests
import re


URL = 'http://m.tureng.com/search/'

while True:

    word = input("-> ")
    r = requests.get(URL+word)
    soup = BeautifulSoup(r.text)
    text = soup.find_all('li')


    category = []
    cat = re.findall(r'<li data-role=\"list-divider\">\r\n(.*?)\r', r.text)
    for i in cat:
        category.append(i.replace(' ', '').replace('(en->tr)', ''))

    count = []
    cnt = re.findall(r'<span class=\"ui-li-count\">\r\n(.*?)\r', r.text)
    for i in cnt:
        count.append(i.replace(' ', '').replace('</span></li>', ''))


    loop = 0


    for i in range(len(category)):
        print('\n\033[94m  '+category[i])
        for j in range(int(count[i])+1):
            if '(en->tr)' not in text[loop].get_text():
                print('\033[92m'+'\t'+text[loop].get_text().replace('\r', '').replace('\n', ''))
            loop += 1

