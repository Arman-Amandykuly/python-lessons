from connect import config
import psycopg2
def delete_part(part_id):
    conn = None
    delete_sql = "DELETE FROM parts WHERE part_id = %s;"
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(delete_sql, (part_id,))
        rows_deleted = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return rows_deleted
if __name__ == "__main__":
    deleted_rows = delete_part(2)
    print("The number of deleted rows: ",deleted_rows)