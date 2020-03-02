#!/usr/bin/env python3

import psycopg2

def record(weather):
    try:
        connection = psycopg2.connect(user = "pi",
                                    password = "C0NN3CTdis",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "pi")
        cursor  = connection.cursor()

        postgres_insert_query = """INSERT INTO flowering_weather (timestamp, temperature, humidity) VALUES (now(),%s, %s)"""
        record_to_insert = (weather['temperature'], weather['humidity'])
        
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Weather record successfully recorded into flowering_weather")

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        # closing db connection
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

if __name__ == "__main__":
    pass