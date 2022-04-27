from bs4 import BeautifulSoup
import requests
import json

def scrape_xml_yle():
    url = 'https://feeds.yle.fi/uutiset/v1/recent.rss?publisherIds=YLE_UUTISET'
    artikkelit_lista = []
    
    sivu = requests.get(url)
    soup = BeautifulSoup(sivu.content,features='xml')
    artikkelit = soup.find_all('item')

    for art in artikkelit:
        try:
            otsikko = art.find('title').text
            pubDate = art.find('pubDate').text
            teksti = art.find('content:encoded').text
            t_soup = BeautifulSoup(teksti,features='xml').get_text()
                
            artikkeli = {
                'otsikko': otsikko,
                'pubDate': pubDate,
                'teksti': t_soup
            }
            artikkelit_lista.append(artikkeli)
        except:
            print("Epäonnistunut imurointi")

    print('scrapattu')
    return artikkelit_lista

def scrape_il():
    url = 'https://www.iltalehti.fi/rss/uutiset.xml'
    sivu = requests.get(url)
    soup = BeautifulSoup(sivu.content,features='xml')
    
    artikkelit = soup.find_all('item')
    
    

    artikkeli_lista = []
    for art in artikkelit:
        try:
            otsikko = art.find('title').text
            pubDate = art.find('pubDate').text
            linkki = art.find('link').text
    
            
            uusi_sivu = requests.get(linkki)
            soup = BeautifulSoup(uusi_sivu.content,'html.parser')
            body = soup.find('div', class_='article-body')
            
            ps = body.find_all('p')
            
            teksti = ''
            for p in ps:
                teksti = teksti + p.text #Teksti on useissa <p> tageissa, joten ne iteroidaan läpi ja lisätään tekstiin
            artikkeli = {
                'otsikko': otsikko,
                'pubDate': pubDate,
                'teksti': teksti 
            }
            artikkeli_lista.append(artikkeli)
        except:
            print("Jotain väärin")
    print("Kuinka monta artikkelia",len(artikkeli_lista))
    return artikkeli_lista

def to_json(file):
    data = json.dumps(file,ensure_ascii=False,indent=1).encode('utf8')
    print("Data enkoodattu json-utf8 muotoon, decode() muuttaa ihmisluettavaksi")
    return data