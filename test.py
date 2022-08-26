from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory
from libraries.database import Database


data_csv = CsvFactory.main()
data_json = JsonFactory.main()
data_html = HtmlFactory.main()

nbre_enregistrement_html = len(data_html)
nbre_enregistrement_csv = len(data_csv)
nbre_enregistrement_json = len(data_json)


assert nbre_enregistrement_html == 4 , "Le nombre devrait être égal à 4"
assert nbre_enregistrement_csv == 200 , "Le nombre devrait être égal à 200"
assert nbre_enregistrement_json == 200 , "Le nombre devrait être égal à 200"