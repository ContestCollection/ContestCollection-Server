import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

def mkDB():
    #id 추가해야함
    cur.execute("""CREATE TABLE contestData(
    part TEXT, 
    year INTEGER, 
    teamNum INTEGER,
    name TEXT, 
    award TEXT, 
    subTitle TEXT, 
    summary TEXT,
    img TEXT, 
    member1 TEXT, 
    member2 TEXT, 
    member3 TEXT, 
    member4 TEXT, 
    calendar TEXT, 
    githubLink TEXT,
    youtubeLink TEXT, 
    serviceLink TEXT, 
    skills TEXT)
    """)
    # 16개


def insertToDB():
    with open("data.txt", "r", encoding='UTF-8') as f:
        temp = []
        for t in f.readlines():
            t = t.strip()
            if t == "NULL":
                t = None
            temp.append(t)
        cur.execute("INSERT INTO contestData VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", temp)
        conn.commit()
        conn.close()
        print("data insert complete")

def getFromDB():
    cur.execute("SELECT rowid, * FROM contestData")
    rows = cur.fetchall()
    conn.close()

    return rows
