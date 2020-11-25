import sqlite3

def init_db():
    with sqlite3.connect("student.db") as conn:
        c = conn.cursor()

        c.execute("""
                    CREATE TABLE Students(
                        name TEXT,
                        usn TEXT PRIMARY KEY,
                        sem INT
                    );
                    """)
        conn.commit()

        c.execute("""
                    CREATE TABLE Teachers(
                        name TEXT,
                        eno TEXT PRIMARY KEY,
                        subject TEXT
                    );
                    """)
        conn.commit()


init_db()