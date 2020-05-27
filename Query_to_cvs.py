import mysql.connector
from mysql.connector import errorcode
import csv

try:
    cnx = mysql.connector.connect(user='candidate', password='Jy3AAmXk14',
                                  host='155.130.2.3:5433', database='main')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:

    curA = cnx.cursor(buffered=True)

    queryTitle = "SHOW columns FROM MyGuests;"
    curA.execute(queryTitle)
    resultsTitle = curA.fetchall()

    query = "SELECT * FROM MyGuests;"

    curA.execute(query)
    results = curA.fetchall()

    header = []
    for result in resultsTitle:
        header.append(result[0])

    with open('query.csv', 'w', newline='') as f_handle:
        writer = csv.writer(f_handle)

        writer.writerow(header)
        for row in results:
            writer.writerow(row)
finally:
    cnx.close()
