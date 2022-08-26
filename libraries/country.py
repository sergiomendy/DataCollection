import requests


BASE_URL = 'https://restcountries.com/v3.1/all'

class CountryFactory(object):

    @classmethod
    def fetch(cls,url: str):
        with requests.Session() as session:
            data = session.get(url)
        return data.json()
    
    
    @classmethod
    def getCountry(cls,data):
        flags = data.get('flags')
        name = data.get('name')
        common_name = name.get('common')
        flag_png = flags.get('png')
        country = {
            'name':common_name,
            'flag':flag_png
        }
        return country
    
    @classmethod
    def getCountries(cls,data):
        countries= map(cls.getCountry,data)
        return list(countries)

    @classmethod
    def main(cls):
        data = cls.fetch(BASE_URL)
        countries = cls.getCountries(data)
        return countries