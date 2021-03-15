import datetime
import psycopg2

time0 = datetime.datetime.now()

def database_connection():
    """
    Tries to connect to the relational database and prints the connection result.
    """
    global con
    global cur
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

database_connection()


def execute_sql(sql):
    """
    Reads a query and returns the rows of the selected data.

        :param sql: A list with queries.
        :return: A list with records.
    """
    cur.execute(sql)
    records = cur.fetchall()

    print(type(records))
    return records


#======================================= READ/RETURN FUNCTIONS NEED QUERY_LIST:

query_list = ["SELECT * FROM product LIMIT 4;",
              "SELECT COUNT(*) as count, value from properties WHERE key like 'discount' GROUP BY value ORDER BY count LIMIT 10;",
              "SELECT productid as id, value as promo, name as product_name, selling_price as price FROM product pd INNER JOIN properties pp ON pd.id = pp.productid WHERE pp.key like 'discount' ORDER BY id ASC"]


def test_sql(records):
    """
    Reads in a selected set of data as a list and << REDACTED >>

        :param records: A list with records from a selected set of data.
        :return: <<           PLACEHOLDER              >>
    """
    for row in records:
        print(f'product id:  {row[0]}')
        print(f'name: {row[1]}')
        print(f'price:  {row[2]}')
        print(f'brand: {row[3]}\n')

    # put everything in list and return?


test_sql(execute_sql(query_list[0]))


def count_promo_occurences(records):
    for row in records:
        print(row)

count_promo_occurences(execute_sql(query_list[1]))


def select_data(records):
    for row in records:
        print(f'product id:  {row[0]}')
        print(f'promo: {row[1]}')
        print(f'name:  {row[2]}')
        print(f'price: {row[3]}\n')


count_promo_occurences(execute_sql(query_list[2]))

#======================================= READ/RETURN FUNCTIONS NEED QUERY_LIST:

# def create_new_table(table, column, value):
#     sql = """CREATE TABLE IF NOT EXISTS recommendation_%s
#                     (id VARCHAR PRIMARY KEY,
#                      name VARCHAR,
#                      brand VARCHAR,
#                      type VARCHAR,
#                      category VARCHAR,
#                      subcategory VARCHAR,
#                      subsubcategory VARCHAR,
#                      targetaudience VARCHAR,
#                      discount INTEGER,
#                      sellingprice INTEGER,
#                      deal VARCHAR,
#                      description VARCHAR);"""%(column)) # <= column = %s
#
#     cur.execute(sql)

    #create sql


# list_with_tables_to_create = []
# # for i table in list_with_tables_to_create:
#
# create_new_table()







'''
To create tables:

cur.execute("CREATE TABLE top_4? (name VARCHAR(255), address VARCHAR(255))")

'''


con.commit()
cur.close()
con.close()

print(datetime.datetime.now() - time0)   # <= prints how long the program took.