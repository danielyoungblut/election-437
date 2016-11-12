import sqlite3 as sql
import numpy as np

conn = sql.connect("../data/database.sqlite")
c = conn.cursor()

print c.execute("select * from county_facts").fetchone()

conn.close()

#testing github
