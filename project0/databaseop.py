# sqlite3 package to perform database operations
import sqlite3

# createdb function creates a table into database normanpd.db
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

# populatedb function inserts data into incidents table 
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

# status function prints the output list sorted first by the total number of incidents and secondarily, alphabetically by the nature. Each field of the row is separated by the pipe character (|).
def status(db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    query = f'''SELECT nature,COUNT(*) as inc 
                FROM incidents 
                GROUP BY nature
                ORDER BY inc desc, nature asc;'''
    result = cur.execute(query)
    print("Sorted by total number of incidents and nature")
    print("******************************")
    result_desc = dict(result)
    result_sorted = [f"{row}|{result_desc[row]}" for row in result_desc.keys()]
    for row in result_sorted:
       print(row)
    return result_sorted

