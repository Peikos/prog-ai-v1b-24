import psycopg2

connection_string = "host='localhost' dbname='fabriek' user='postgres' password='geheim'"

nr = int(input("Klantnummer? "))
naam = input("Naam? ")
adres = input("Adres? ")
plaats = input("Plaats? ")

with psycopg2.connect(connection_string) as conn: # get a connection with the database

    cursor = conn.cursor() # a ‘cursor’ allows to execute SQL in a db-session

    # query = f"""SELECT klantnr, plaats, adres
    #            FROM Klant
    #            WHERE plaats = '{plaats}';"""

    # Jan','a','b'); DROP TABLE Artikel CASCADE; INSERT INTO Klant VALUES (10000,'

    # query = f"""INSERT INTO Klant VALUES ({nr}, '{naam}', '{adres}', '{plaats}') """

    query = """INSERT INTO Klant VALUES (%s, %s, %s, %s)"""

    cursor.execute(query, (nr, naam, adres, plaats))
    conn.commit() # retrieve the records from the database

# for record in records:
#     print(record)