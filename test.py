import os
import sys
#sys.path.append(os.getcwd()+'/project0')
import pytest
import sqlite3
import main

@pytest.fixture()
def url():
    return "https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-01_daily_incident_summary.pdf"

@pytest.fixture()
def database_name():
    return "normanpd.db"

def test_fetch_incidents(url):
    fetchincidents_test = main.fetchincidents(url)
    assert fetchincidents_test.getcode() == 200

def test_extract_data(url):
    date_time = '1/1/2023 0:06'
    incident_number = '2023-00000001'
    location = '2000 ANN BRANDEN BLVD',
    nature = 'Transfer/Interfacility', 
    incident_ori = 'EMSSTAT'
    fetchincidents_test = main.fetchincidents(url)
    incidents = main.extractdata.extractincidents(fetchincidents_test)
    count = False
    for i in incidents:
	if i == [date_time, incident_number, location, nature, incident_ori]:
		count = True
		break
    assert len(incidents) > 0
    assert count


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


def test_populatedb(database_name):
    incidents = [['1/1/2023 0:06', '2023-00000001', '2000 ANN BRANDEN BLVD', 'Transfer/Interfacility', 'EMSSTAT']]
    db = main.databaseop.createdb(database_name)
    main.databaseop.populatedb(db, incidents)
    con = sqlite3.connect(database_name)
    cur = con.cursor()
    result = cur.execute("SELECT * FROM incidents;").fetchall()
    con.commit()
    con.close()
    assert len(result) > 0


def test_status(database_name):
    result = main.databaseop.status(database_name)
    t1 = []
    t2 = []
    check = True
    sort_check = True
    for i in res:
        if '|' not in i:
            check = False
            break
        else:
            t1.append(i.split("|")[0])
            t2.append(i.split("|")[0])

    t2.sort()
    if t1 == t2:
        sort_check = True
    else:
        sort_check = False

    assert len(result) > 0
    assert check == True
    assert sort_check == True
