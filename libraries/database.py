import sqlite3

class Db:
    @staticmethod
    def getConnection():
        connection = sqlite3.connect("Databases/data.db")
        return connection

class Database:
    def __init__(self):
        self.__connection = Db.getConnection()
        self.__createTable()
    
    def __createTable(self):
        print("Creating the table.....")
        connection = self.__connection
        cursor = connection.cursor()
        with open('script.sql','r') as f:
            file = f.read()
        cursor.executescript(file)
        print("Table created.....")
        connection.commit()
    
    def insertDataToDatabase(self,data):
        print("Inserting data to the database")
        keys = tuple(data[0].keys())
        values = [tuple(elt.values()) for elt in data]
        requete = f"INSERT INTO person {keys} values(?,?,?,?,?,?,?,?,?,?,?)"

        connection = self.__connection
        cursor = connection.cursor()
        cursor.executemany(requete,values)
        num = cursor.rowcount
        print(f"{num} rows inserted")
        connection.commit()
    
    @classmethod
    def getValues(cls):
        connection = Db.getConnection()
        cursor = connection.cursor()
        requete = "Select * from person"
        cursor.execute(requete)
        keys = [description[0] for description in cursor.description]
        values = cursor.fetchall()
        connection.close()
        return cls.toListOfDicts(keys,values)
    
    @classmethod
    def toListOfDicts(cls,keys,values):
        liste = []
        length = len(keys)
        for value in values:
            elt = {keys[i]:value[i] for i in range(length)}
            liste.append(elt)
        return liste
    
    