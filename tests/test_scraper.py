import unittest
from main.src.scraper import scrape_xml_yle, to_json
from main.src.scraper import scrape_il
from main.src.scraper import to_json

class TestMethods(unittest.TestCase):
    def test_ylescraper(self):
        artikkelit = scrape_xml_yle()
        #Varmista,että artikkeleja on imuroitu
        assert len(artikkelit) > 0
        #Varmista, että palautettu tyyppi on lista, jotta jsoniksi muuttaminen onnistuu
        assert type(artikkelit) == list
        #Katso, että kaikkiin on tallentunut kaikki tiedot: Otsikko, julkaisupvm, teksti
        for art in artikkelit:
            self.assertTrue(len(art) == 3) 

    def test_ilscraperself(self):
        artikkelit = scrape_il()

        assert len(artikkelit) > 0

        assert type(artikkelit) == list

        for art in artikkelit:
            self.assertTrue(len(art) == 3) 

    def test_json(self):
        import json
        file = scrape_xml_yle()
        data = to_json(file)

        self.assertIsInstance(data,bytes)
        loaded = json.loads(data)
        

        self.assertEqual(file,loaded) #Katsotaan, että jsoniksi muuttaminen ja siitä palauttaminen ei muuta dataa



