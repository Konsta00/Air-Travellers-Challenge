from database import db_connection

connection = db_connection.connect_to_database()

def get_closest_airports(current_airport):

    # fetch coordinates for current airport
    sql = 'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s ;'
    lat, lon = coords = db_connection.fetch_one(connection, sql, current_airport)

    closest_airports_sql = f'''
    SELECT name, latitude_deg, longitude_deg,
            6371 * ACOS(
                COS(RADIANS({lat})) * COS(RADIANS(latitude_deg)) 
                * COS(RADIANS({lon} - longitude_deg)) +
                SIN(RADIANS({lat})) * SIN(RADIANS(latitude_deg))
            ) AS Distance_KM
        FROM
            airport
        ORDER BY
            Distance_KM ASC
        LIMIT 10;
    '''

    closest_airports_list = db_connection.fetch_data(connection, closest_airports_sql)
    return closest_airports_list

    # FETCH 10 CLOSEST AIRPORT FROM DATABSE, APPEND TO LIST AND FINALLY RETURN THE LIST. IN MAIN CODE SET 


    



get_closest_airports('EHAM')
