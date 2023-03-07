import sqlite3

def createdb(dbname='normanpd.db'):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS incidents(
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
    nature TEXT,
    incident_ori TEXT); ''')
    con.commit()
    con.close()
    return dbname

def populatedb(db, incidents):
    con = sqlite3.connect(db)
    cur = con.cursor()
    query = f"INSERT INTO incidents(incident_time,incident_number,incident_location,nature,incident_ori) VALUES(?,?,?,?,?)"

    for i in range(0, len(incidents)):
        for j in range(0, len(incidents[i])):
            date, innumber, location, nature, ori = [k for k in incidents[i][j]]
            cur.execute(query, (date, innumber, location, nature, ori))
    con.commit()
    con.close()

def status(db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    query = f'''SELECT nature,COUNT(*) as inc 
                FROM incidents 
                GROUP BY nature
                ORDER BY inc desc, nature asc;'''

    result = cur.execute(query)
    print("Sorted by Nature")
    print("*" * 100)
    result_sorted = []
    result_desc = dict(result)
    for row in result_desc.keys():
        print(row, "|", result_desc[row])
        result_sorted.append(row + "|" + str(result_desc[row]))
    return result_sorted
