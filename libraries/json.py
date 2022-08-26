import json
from libraries.currency import Currency
from .utils import Utils
from libraries.country import CountryFactory

BASE_URL = 'DATABASES/data-zIybdmYZoV4QSwgZkFqvC.json'


class JsonFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = json.load(file)
            file.close()
        return data

    @classmethod
    def addSalary(cls, data):
        def salary(x):
            START = 200000
            FINAL = 1000000
            x['salary'] = Utils \
                .randomize(START, FINAL)
            x['salary'] = float(x['salary'])
            return x
        data = map(salary, data)
        return list(data)

    @classmethod
    def addAge(cls, data):
        def age(x):
            START = 18
            FINAL = 100
            x['age'] = Utils \
                .randomize(START, FINAL)
            x['age'] = int(x['age'])
            return x
        data = map(age, data)
        return list(data)

    @classmethod
    def naming(cls, data):
        def name(x):
            x['name'] = x['name'].split(' ')
            last_name = x['name'][-1].upper()
            first_name = x['name'][0].capitalize()
            x['name'] = ' '.join([first_name, last_name])
            return x
        data = map(name, data)
        return list(data)
    
    @classmethod
    def addCurrency(cls, data):
        currencies = ['Euro','Dollar us','Yen japonais']
        def currency(row):
            START = 0
            FINAL = 2
            row['currency'] = currencies[Utils.randomize(START, FINAL)]
            return row
        data = map(currency,data)
        return list(data)

    @classmethod
    def addSalaryXOF(cls, data):
        currencies = Currency.currencies()
        def salaryXOF(x):
            salary = x.get('salary')
            devise = x.get('currency')
            x['salary (XOF)'] = Utils.convertToXOF(salary,devise,currencies)
            return x
        data = map(salaryXOF, data)
        return list(data)
    
    @classmethod
    def addCountryAndFlag(cls, data):
        countries = CountryFactory.main()
        def country(row):
            START = 0
            FINAL = len(countries)-1
            index = Utils.randomize(START, FINAL)
            country = countries[index]
            row['country'] = country.get('name')
            row['flag'] = country.get('flag')
            return row
        data = map(country,data)
        return list(data)

    @classmethod
    def main(cls):
        data = cls.openFile()
        data = cls.addSalary(data)
        data = cls.addAge(data)
        data = cls.naming(data)
        data = cls.addCurrency(data)
        data = cls.addSalaryXOF(data)
        data = cls.addCountryAndFlag(data)
        return data
