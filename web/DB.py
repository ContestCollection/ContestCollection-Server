import sqlite3
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

path = os.path.abspath("database.db")
conn = sqlite3.connect(path, check_same_thread=False)
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
        #conn.close()
        print("data insert complete")

def getFromDB():
    cur.execute("SELECT rowid, * FROM contestData")
    rows = cur.fetchall()
    #conn.close()

    return rows

def getFromDB2(part, year, id):
    if part and year:
        cur.execute(f"SELECT rowid, * FROM contestData WHERE part = '{part}' AND year = '{year}'")
    elif part:
        cur.execute(f'SELECT rowid, * FROM contestData WHERE part = "{part}"')
    elif year:
        cur.execute(f"SELECT rowid, * FROM contestData WHERE year = '{year}'")
    elif id:
        cur.execute(f"SELECT rowid, * FROM contestData WHERE rowid = '{id}'")

    rows = cur.fetchall()
    #conn.close()

    return rows