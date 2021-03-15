import datetime
import psycopg2

time0 = datetime.datetime.now()
content = ['category', 'sub_category', 'sub_sub_category', 'properties']
sub_sub_category = ['Pijnstillers', 'Multivitaminen', 'Shampoo', 'Kat', 'Toiletpapier_en_vochtige_doekjes', 'Elektronica_accessoires', 'Condooms', 'Batterijen', 'Kunstgebitverzorging', 'Wasverzachter', 'Tandenstokers_floss_en_ragers', 'Meubels', 'Overige_dierverzorging', 'Haaraccessoires', 'Lenzenvloeistof', 'Feestartikelen', 'Wattenschijfjes_en_wattenstaafjes', 'Reisziekte', 'Textielverf', 'Pleisters', 'Accessoires', 'Zwangerschap', 'Gewrichten', 'Oogschaduw', 'Reiniging_vaatwasser', 'Nagellakremovers', 'Schoenen_slippers_en_sloffen', 'Voetschimmel', 'Foundation_en_concealer', 'Blush', 'Media', 'Scheerschuim_en_scheergel', 'Kinderkleding', 'Geschenksets', 'Zwangerschapsvitamines', 'Homeopathisch', 'Overige_huishoudelijke_artikelen', 'Mondverfrissers', 'Bad_en_douche', 'Kaarsen', 'Huishoudelijke_apparaten', 'Voetdeodorant', 'Aftershave', 'Babyhaartjes_bad_en_douche', 'Afwasmiddel', 'Kaarten', 'Poeder', 'Carnaval', 'Keukenpapier', 'Nagellak', 'Mondwater_en_spray', 'Sieraden_en_bijoux', 'Make_up_remover_en_reiniging', 'Bandages_en_windsels', 'Dames_nachtmode', 'Vlekkenverwijderaars', 'Onzuivere_huid_en_acne', 'Zwemluiers', 'Koffie', 'Deodorant', 'Tampons', 'Overige_voedingssuplementen', 'Haarkuur_en_haarmasker', 'Kappersproducten', 'Schoonmaken', 'Muziek', 'Knutselen_en_hobby', 'Glijmiddelen_en_seksspeeltjes', 'Kerst', 'Kantoor_benodigdheden', 'Dames_brillen', 'Oor_en_mond', 'Chips', 'Anti_lekbekers', 'Speelgoed', 'Herengeuren', 'Bordspellen', 'Highlighters_en_bronzers', 'Toiletblokken', 'Luchtwegen_en_verkoudheid', 'Weerstand', 'Enkelvoudige_vitaminen', 'Damesgeuren', 'Sportverzorging', 'Lipliner', 'Dames_kleding', 'Dvd_en_Blue_ray', 'Luierbroekjes_en_pyjamabroekjes', 'Tissues_en_zakdoekjes', 'Lipverzorging', 'Botten', 'Overige_elektronika', 'Watten', 'Heren_nachtmode', 'Scheermesjes', 'Make_up_accessoires', 'Lenzen', 'Maaltijdvervangers', 'Blaas', 'Baby_accessoires', 'Sportdranken', 'Sportvoeding', 'EHBO', 'Oogcreme_en_serum', 'Cartridges', 'Mini_tandpasta', 'Ontspanning_en_rust', 'Babydoekjes', 'Kunstnagels', 'Foto_en_film', 'Gezichtsmasker_man', 'Spierwrijfmiddelen', 'Man', 'Boeken', 'Baby_speelgoed', 'Flesvoeding', 'Lampen', 'Insectenbestrijding', 'Babykleding', 'Mineralen', 'Haarserum', 'Keuken_artikelen', 'Baby_en_kinderaccessoires', 'Luizen', 'Tandpasta', 'Heren_brillen', 'Verzorgende_voetcremes', 'Dames_ondergoed', 'Mascara', 'Kinderbestek', 'Flessen_en_flessenspenen', 'Reiniging', 'Eelt_en_harde_huid', 'Supplementen', 'Dames_accessoires', 'Ontharingscreme_wax_en_hars', 'Pasen', 'Vaatwastabletten', 'Outdoor_en_vrije_tijd', 'Natuurlijke_gezondheid', 'Beeld_en_geluid', 'Fopspenen', 'Handcremes', 'Tablets_en_computers', 'Huidverzorging_en_koortslip', 'Koffers', 'Nachtcreme', 'Vakantie', 'Leesbrillen', 'Maandverband', 'Mini_scheerschuim_en_scheergel', 'Inlegkruisjes', 'Intiemverzorging', 'Vaginale_schimmel', 'Wratten', 'Tuinartikelen', 'Mini_bad_en_douche', 'Tassen', 'Mama_verzorging', 'Voetverzorging', 'Hond', 'Verlichting', "Vibrators_en_dildos", 'Uiterlijk', 'Creme', 'Wenkbrauwproducten', 'Haarstyling', 'Wasmiddel', 'Oordoppen', 'Handzeep_en_handgel', 'Lipgloss', 'Kalknagels', 'Energie', 'Snacks_en_snoep', 'Stoppen_met_roken', 'Incontinentie', 'Mini_olie_en_lotion', 'Heren_ondergoed', 'Wondontsmetting', 'Kind', 'Luiers', 'Gezichtsmasker', 'Thee', 'Zonnebrand_en_aftersun', 'Lipstick', 'Energy_drank', 'Zwangerschapstest_en_ovulatietest', 'Telefonie', 'Woonaccessoires', 'Heren_accessoires', 'Aambeien', 'Scheren', 'Dagcreme', 'Mini_shampoo_en_conditioner', 'Haarkleuring', 'Overige_dranken', 'Wondverzorging', 'Allergieen', 'Bodylotion_en_bodymilk', 'Hart_en_visolie', 'Toilettassen', 'Elektrische_tandenborstels', 'Toiletreinigers', 'Halloween', 'Huishoudelijk_textiel', 'Tandenborstels', 'Panties_en_sokken', 'Luchtverfrissers', 'Valentijn', 'Sportartikelen', 'Conditioner', 'Mini_deodorant_en_geuren', 'Persoonlijke_verzorging', 'Sokken', 'Baby_huidverzorging', 'Scheerapparaten', 'Patty_Brard_Collectie', 'Spijsvertering', 'Mini_haarstyling', 'Reiniging_man']


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


#======================================= CREATE TABLES:

def create_new_table(table):
    """
    Creates new tables for every different kind of recommendation.

        :param table: A string that represents the name of the table.
        :return: None.
    """
    sql = ("CREATE TABLE IF NOT EXISTS rec_%s (id VARCHAR PRIMARY KEY, promo VARCHAR, product_name VARCHAR, category VARCHAR, sub_category VARCHAR, sub_sub_category VARCHAR, target_audience VARCHAR, price int);"%(table))
    cur.execute(sql)


for i in sub_sub_category:
     create_new_table(i)


#======================================= READ/RETURN FUNCTIONS NEED QUERY_LIST:

def select_data(sql):
    """
    Reads a query and returns the rows of the selected data.

        :param sql: A list with queries as strings.
        :return: A list with records as tuples.
    """
    cur.execute(sql)
    records = cur.fetchall()

    return records

query = "SELECT productid as id, value as promo, name as product_name, category, sub_category, sub_sub_category, gender as target_audience, selling_price as price FROM product pd INNER JOIN properties pp ON pd.id = pp.productid WHERE pp.key like 'discount' ORDER BY id ASC LIMIT 4;"


def execute_sql(records):
    """

        :param records: A list with records as tuples.
        :return: None.
    """
    for row in records:
        print(row)

        #insert into table.


#======================================= READ/RETURN FUNCTIONS NEED QUERY_LIST:


con.commit()
cur.close()
con.close()

print(datetime.datetime.now() - time0)   # <= prints how long the program took.