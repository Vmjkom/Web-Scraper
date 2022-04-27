import unittest
from main.src.scraper import scrape_xml_yle
from main.src.scraper import scrape_il

def test_ylescraper():
    artikkelit = scrape_xml_yle()
    #Varmista,että artikkeleja on imuroitu
    assert len(artikkelit) > 0
    #Varmista, että palautettu tyyppi on lista, jotta jsoniksi muuttaminen onnistuu
    assert type(artikkelit) == list
    #Katso, että kaikkiin on tallentunut kaikki tiedot: Otsikko, julkaisupvm, teksti
    for art in artikkelit:
        assert len(art) == 3

def test_ilscraper():
    artikkelit = scrape_il()

    assert len(artikkelit) > 0

    assert type(artikkelit) == list

    for art in artikkelit:
        assert len(art) == 3

