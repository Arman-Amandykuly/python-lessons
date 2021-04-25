import psycopg2
from connect import config
def create_tables():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(params)
        commands = (
            """CREATE TABLE [IF NOT EXISTS] vendors(
                vendor_id SERIAL PRIMARY KEY,
                vendor_name VARCHAR(255) NOT NULL
            )""",
            """CREATE TABLE [IF NOT EXISTS] parts(
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
            )""",
            """CREATE TABLE [IF NOT EXISTS] part_drawings(
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part id),
                REFERENCES parts(part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
            )""",
            """CREATE TABLE [IF NOT EXISTS] vendor_parts(
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id, part_id)
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )"""
        )
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
