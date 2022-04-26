from bs4 import BeautifulSoup
import requests
import json

def scrape_yle(url):

    url = 'yle.fi/uutiset'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")
    #test
    #test
    python_jobs = results.find_all(
        "h2", string=lambda text: "python" in text.lower()
    )

    python_job_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]
    #print(python_job_elements)
    for job_element in python_job_elements:
        title_element = job_element.find("h2", class_="title is-5")
        company_element = job_element.find("h3", class_="subtitle is-6 company")
        location_element = job_element.find("p", class_="location")
        print("Title:",title_element.text.strip())
        print("Company:",company_element.text.strip())
        print("Location:",location_element.text.strip())
        print()

def scrape_xml_yle():
    url = 'https://feeds.yle.fi/uutiset/v1/recent.rss?publisherIds=YLE_UUTISET'
    artikkelit_lista = []
    try:
        sivu = requests.get(url)
        soup = BeautifulSoup(sivu.content,features='xml')
        artikkelit = soup.find_all('item')

        for art in artikkelit:
            otsikko = art.find('title').text
            pubDate = art.find('pubDate').text
            teksti = art.find('content:encoded').text
            t_soup = BeautifulSoup(teksti).get_text()
            
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

def to_json(file):
    data = json.dumps(file,ensure_ascii=False,indent=1).encode('utf8')
    print("Data enkoodattu json-utf8 muotoon, decode() muuttaa ihmisluettavaksi")
    return data