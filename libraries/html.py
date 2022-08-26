from libraries.country import CountryFactory
from libraries.currency import Currency
from .utils import Utils
from bs4 import BeautifulSoup

BASE_URL = 'DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'

class HtmlFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = file.read()
            data = BeautifulSoup(data,'html.parser')
        return data
    
    @classmethod
    def getRows(cls,data):
        rows = data.find_all('tr')
        return rows
    
    @classmethod
    def getKeys(cls,headers_row):
        headers = headers_row.find_all('th')
        keys = [header.getText().lower() for header in headers]
        return keys
    
    @classmethod 
    def getValues(cls,data_rows):
        values = []
        for row in data_rows:
            datas = row.find_all('td')
            value = [data.getText() for data in datas]
            values.append(value)
        return values

    @classmethod
    def getListOfDicts(cls,keys,values):
        liste = []
        length = len(keys)
        for value in values:
            elt = {keys[i]:value[i] for i in range(length)}
            liste.append(elt)
        return liste
    
    @classmethod
    def addSalary(cls, data):
        def salary(x):
            START = 200000
            FINAL = 1000000
            x['salary'] = Utils.randomize(START, FINAL)
            x['salary'] = float(x['salary'])
            return x
        data = map(salary, data)
        return list(data)

    @classmethod
    def addAge(cls, data):
        def age(x):
            START = 18
            FINAL = 100
            x['age'] = Utils.randomize(START, FINAL)
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
    def addAddress(cls, data):
        addresses = ["119-1771 In St.","754-1722 Non Road","Ap #909-1330 Dui St.","P.O. Box 534, 6603 Accumsan Rd.","4454 Lacus. Av."]
        def currency(row):
            START = 0
            FINAL = len(addresses) - 1
            row['address'] = addresses[Utils.randomize(START, FINAL)]
            return row
        data = map(currency,data)
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
        def salaryXOF(x):
            salary = x.get('salary')
            devise = x.get('currency')
            currencies = Currency.currencies()
            x['salary_xof'] = Utils.convertToXOF(salary,devise,currencies)
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
        rows = cls.getRows(data)
        headers_row = rows[0]
        datas_rows = rows[1:]
        keys = cls.getKeys(headers_row)
        values = cls.getValues(datas_rows)
        data = cls.getListOfDicts(keys,values)
        data = cls.addSalary(data)
        data = cls.addAge(data)
        data = cls.naming(data)
        data = cls.addAddress(data)
        data = cls.addCurrency(data)
        data = cls.addSalaryXOF(data)
        data = cls.addCountryAndFlag(data)
        return data