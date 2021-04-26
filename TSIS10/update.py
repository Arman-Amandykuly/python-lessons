from connect import config
import psycopg2
def update_vendor(vendor_id,vendor_name):
    params = config()
    conn = None
    try:
        sql_update = """UPDATE vendors
                       SET vendor_name = %s
                        WHERE vendor_id = %s"""
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql_update,(vendor_name,vendor_id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return updated_rows
if __name__ == "__main__":
    update_vendor(1,"3M Corp")