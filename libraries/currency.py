from bs4 import BeautifulSoup
import requests


BASE_URL = "https://www.bceao.int/fr/cours/cours-des-devises-contre-Franc-CFA-appliquer-aux-transferts"

class Currency(object):
    
    @classmethod
    def fetcher(cls,url):
        return requests.get(url).text

    @classmethod
    def getRows(cls,html):
        data = BeautifulSoup(html,features="html.parser")
        rows = data.find_all('tr')
        return rows[1:]

    @classmethod
    def getCurrencies(cls,rows):
        currencies = []
        for row in rows:
            datas = row.find_all('td')
            currency = {
                'devise':datas[0].getText(),
                'achat':float(datas[1].getText().replace(',','.')),
                'vente':float(datas[2].getText().replace(',','.'))
            }
            currencies.append(currency)

        return currencies

    @classmethod
    def currencies(cls):
        html = cls.fetcher(BASE_URL)
        rows = cls.getRows(html)
        currencies = cls.getCurrencies(rows)
        return currencies
