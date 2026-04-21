import pandas as pd
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "practice.db")

def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    
    if not query.upper().startswith("SELECT"):
        print("Warning! Only SELECT statements allowed.")
        conn.close()
        return
    else:
        df = pd.read_sql_query(query,conn)
    conn.close()
    print(df)
    print("Query ran successfully.")
    return

if __name__=="__main__":
    run_query("SELECT * FROM players")
