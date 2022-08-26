DROP TABLE IF EXISTS person;

CREATE TABLE person (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT, 
    phone TEXT,
    email TEXT, 
    address TEXT, 
    latlng TEXT,
    salary FLOAT, 
    age INTEGER,
    currency TEXT,  
    salary_xof FLOAT, 
    country TEXT, 
    flag TEXT
);
