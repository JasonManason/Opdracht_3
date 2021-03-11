import datetime
import psycopg2

time0 = datetime.datetime.now()

try:
    con = psycopg2.connect(
        host="localhost",
        database="huwebshop",
        user="postgres",
        password="admin",
    )
    cur = con.cursor()
    print('Database connection succes')
except:
    print('Something went wrong with the database connection')


def execute_sql(sql):
    cur.execute(sql)
    records = cur.fetchall()

    return records


query_list = ["SELECT * FROM product LIMIT 4", "SELECT COUNT(*) as count, value from properties WHERE key like 'discount' GROUP BY value ORDER BY count"]


def test_sql(records):
    for row in records:
        print(f'product id:  {row[0]}')
        print(f'name: {row[1]}')
        print(f'price:  {row[2]}\n')


test_sql(execute_sql(query_list[0]))


# def count_promo_occurences():
#     sql = "SELECT COUNT(*) as count, value from properties WHERE key like 'discount' GROUP BY value ORDER BY count"
#     cur.execute(sql)
#
#     records = cur.fetchall()
#
#     for row in records:
#         print(row)

# count_promo_occurences()

'''
To create tables:

cur.execute("CREATE TABLE top_4? (name VARCHAR(255), address VARCHAR(255))")

'''


con.commit()
cur.close()
con.close()

print(datetime.datetime.now() - time0)   # <= prints how long the program took.