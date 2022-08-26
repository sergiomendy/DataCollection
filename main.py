from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory
from libraries.database import Database
from fastapi import FastAPI

data1 = CsvFactory.main()
data2 = JsonFactory.main()
data3 = HtmlFactory.main()
data = Utils.concatenate(data1,data2,data3)
db = Database()
db.insertDataToDatabase(data)

app = FastAPI()
@app.get("/persons")
def read_root():
    return Database.getValues()
