import csv
import mysql.connector


with mysql.connector.connect(user='sql11499615', password='LIse97RayX', host='sql11.freemysqlhosting.net', database='sql11499615') as connection:
    cursor = connection.cursor()

    with open('cities.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                previous_position = int(row['2021'])
            except:
                previous_position = 0
            sql = f"""INSERT INTO
            city(name, country, position, previous_position)
            VALUES('{row['City']}', '{row['Country']}', {int(row['2022'])}, {previous_position})
            """
            cursor.execute(sql)

        connection.commit()