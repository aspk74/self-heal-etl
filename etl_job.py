import sqlite3

def run_etl():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    
    try:
        # Faulty SQL: wrong column name
        cursor.execute("SELECT non_existing_column FROM users")
        rows = cursor.fetchall()
        print("Data:", rows)
    except Exception as e:
        raise RuntimeError(f"ETL Job failed: {str(e)}")
    finally:
        conn.close()
