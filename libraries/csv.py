from .utils import Utils
import pandas as pd
from libraries.currency import Currency
from libraries.country import CountryFactory

BASE_URL = 'DATABASES/data-_zJ9Zko2Dh1LYlNNgALKE.csv'


class CsvFactory(object):
    @classmethod
    def openFile(cls):
        data = pd.read_csv(
            BASE_URL,
            encoding='utf-8')
        return data

    @classmethod
    def addSalary(cls, data):
        START = 200000
        FINAL = 1000000
        data['salary'] = float(0)
        data['salary'] = data['salary'] \
            .apply(lambda x: Utils.randomize(START, FINAL))
        return data

    @classmethod
    def addAge(cls, data):
        START = 18
        FINAL = 100
        data['age'] = 0
        data['age'] = data['age'] \
            .apply(lambda x: Utils.randomize(START, FINAL))
        return data

    @classmethod
    def naming(cls, data):
        data['name'] = data['name'] \
            .apply(Utils.x)
        return data
    
    @classmethod
    def addCurrency(cls, data):
        START = 0
        FINAL = 2
        currencies = ['Euro','Dollar us','Yen japonais']
        data['currency'] = None
        
        data['currency'] = data['currency'] \
            .apply(lambda x:currencies[Utils.randomize(START, FINAL)])
        return data
    
    @classmethod
    def addSalaryXOF(cls, data):
        currencies = Currency.currencies()
        def salaryXOF(x):
            salary = x.get('salary')
            devise = x.get('currency')
            x['salary_xof'] = Utils.convertToXOF(salary,devise,currencies)
            return x
        data = list(data.T.to_dict().values())
        data = map(salaryXOF, data)
        data = pd.DataFrame(data)
        return data
    
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
        data = list(data.T.to_dict().values())
        data = map(country,data)
        data = pd.DataFrame(data)
        return data

    @classmethod
    def main(cls):
        data = cls.openFile()
        data = cls.addSalary(data)
        data = cls.addAge(data)
        data = cls.naming(data)
        data = cls.addCurrency(data)
        data = cls.addSalaryXOF(data)
        data = cls.addCountryAndFlag(data)
        data = data \
            .T \
            .to_dict() \
            .values()
        return list(data)
