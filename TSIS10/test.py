from connect import config
import psycopg2
def test(part_id):
    conn = None
    sql = "SELECT * FROM parts WHERE part_id = %s"
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql,(part_id,))
        for i in cur.fetchall():
            print(i)
        conn.commit()
        cur.close()
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == "__main__":
    import sys
    if len(sys.argv)>2:
        for i in sys.argv[1:]:
            test(int(i))
    else:
        test(1)