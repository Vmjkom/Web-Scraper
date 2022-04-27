from bs4 import BeautifulSoup
import requests
import json
"""
Käytetään requests kirjastoa tekemään HTTP get pyyntö Url:iin.
Beautifulsoup kirjastoa käytetään parsettamaan xml sivu.
Sivusta etsitään yksittäiset uutiset, josta otetaan ylös otsikko, julkaisupäivämäärä sekä teksti.
Artikkelit tallennetaan dict tiedostoon, jotka kootaan listaan
"""
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
            t_soup = BeautifulSoup(teksti,features='xml').get_text() # teksti on <p> tagien sisällä, joten parsetetaan uudestaan jolloin jää vain teksti
                
            artikkeli = {
                'otsikko': otsikko,
                'pubDate': pubDate,
                'teksti': t_soup
            }
            artikkelit_lista.append(artikkeli)
        except:
            print("Epäonnistunut imurointi")

    print(f'Scrapattu {len(artikkelit_lista)} uutista yleltä, pvm: {list(artikkelit_lista[0].values())[1]}')
    return artikkelit_lista
"""
Muuten samanlainen, kuten ylen metodi, 
mutta iltalehden rss syötteestä joudutaan kaivamaan teksti
menemalla linkin kautta itse uutiseen.

"""
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
                teksti = teksti + p.text    #Teksti on useissa <p> tageissa, joten ne iteroidaan läpi ja lisätään tekstiin
            artikkeli = {
                'otsikko': otsikko,
                'pubDate': pubDate,
                'teksti': teksti 
            }
            artikkeli_lista.append(artikkeli)
        except:
            print("Jotain väärin")
    print(f'Scrapattu {len(artikkeli_lista)} uutista yleltä, pvm: {list(artikkeli_lista[0].values())[1]}')
    return artikkeli_lista


def to_json(file):
    data = json.dumps(file,ensure_ascii=False,indent=1).encode('utf8')
    print("Data enkoodattu json-utf8 muotoon, decode() muuttaa ihmisluettavaksi")
    return data