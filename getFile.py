from bs4 import BeautifulSoup
import urllib.request as req
import urllib

dir = './downloads/'

fileName = '2ndtrax'#다운로드한 파일을 저장할 이름
extension = '.zip.'#다운로드 파일 확장자

url = 'https://jun1517.tistory.com/758'
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')

for href in soup.find("div", class_="contents_style").find_all('figure','fileblock'):
    #print(href.find("a")["href"])
    #print(href.find("a")["href"].split('.')[-1])
    req.urlretrieve(href.find("a")["href"], dir+fileName+extension+href.find("a")["href"].split('.')[-1])