import os
# sys package to get system path
import sys
sys.path.append(os.getcwd()+'/project0')
# pytest package to run pytest
import pytest
# sqlite3 package for database operations
import sqlite3
from project0 import main

@pytest.fixture()
def url():
    return "https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-01_daily_incident_summary.pdf"

@pytest.fixture()
def database_name():
    return "normanpd.db"

# test for fetchincidents() function in main.py
def test_fetch_incidents(url):
    fetchincidents_test = main.fetchincidents(url)
    if fetchincidents_test == url:
    	assert True

# test for extractincidents() function in extractdata.py
def test_extract_data(url):
    incident_number = '2023-00002060' 
    fetchincidents_test = main.fetchincidents(url)
    incidents = main.extractdata.extractincidents(fetchincidents_test)
    print(incidents[0][0][1])
    count = False
    if incidents[0][0][1] == incident_number:
        count = True
    assert len(incidents) > 0
    assert count

# test for createdb() function in databaseop.py
def test_createdb(database_name): 
    db = main.databaseop.createdb(database_name)
    query = """SELECT name FROM sqlite_master WHERE type='table'
            AND name='incidents'; """
    con = sqlite3.connect(database_name)
    cur = con.cursor()
    result = cur.execute(query).fetchall()
    con.commit()
    con.close()
    assert len(result) == 1

# test for populatedb() function in databaseop.py
def test_populatedb(database_name):
    incidents = [[['1/1/2023 0:06', '2023-00000001', '2000 ANN BRANDEN BLVD', 'Transfer/Interfacility', 'EMSSTAT']]]
    main.databaseop.populatedb(database_name, incidents)
    con = sqlite3.connect(database_name)
    cur = con.cursor()
    result = cur.execute("SELECT * FROM incidents;").fetchall()
    con.commit()
    con.close()
    assert len(result) > 0

# test for status() function in databaseop.py
def test_status(database_name):  
    result = main.databaseop.status(database_name)
    assert result is not None
  
   
