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


sql = "SELECT * FROM product LIMIT 4"
product = cur.execute(sql)

records = cur.fetchall()

for row in records:
    print('product id: ', row[0])
    print('name: ', row[1])
    print(f'price:  {row[2]}\n')


con.commit()
cur.close()
con.close()

print(datetime.datetime.now() - time0)   # <= prints how long the program took.