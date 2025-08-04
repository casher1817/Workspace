import requests
from bs4 import BeautifulSoup

# PTT Gossiping board URL
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
# PTT requires an over18 cookie
cookies = {'over18': '1'}

res = requests.get(url, cookies=cookies)
soup = BeautifulSoup(res.text, 'html.parser')

for post in soup.select('.r-ent'):
    title_tag = post.select_one('.title a')
    if title_tag:
        title = title_tag.text.strip()
        link = 'https://www.ptt.cc' + title_tag['href']
        author = post.select_one('.author').text.strip()
        print(f'Title: {title}\nAuthor: {author}\nLink: {link}\n')