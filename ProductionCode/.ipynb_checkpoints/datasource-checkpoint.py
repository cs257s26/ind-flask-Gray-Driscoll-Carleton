import psycopg2 as ps
from ProductionCode import psqlconfig as config


#modified moodle code to find the literature rate over time in a set country
def lit_over_time_country(connection, start_year, end_year, country):
        try:
            cursor = connection.cursor()
            #returns the year and the average literacy rate during two different years in a certain country
            query = """
                SELECT
                    year, 
                    entity,
                    AVG(literacy_rate)
                    FROM education_data
                    WHERE year >= %s AND year <= %s AND entity = %s
                    GROUP BY year, entity;
                    """
            cursor.execute(query, (start_year, end_year, country))
            return cursor.fetchall()
    
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None


def education_query(connection, start_year, country):
    try: 
        cursor = connection.cursor()

        query = """
            SELECT 
                year, 
                entity, 
                avg_years_education
            FROM education_data
            WHERE entity = %s AND year = %s;
        """
        cursor.execute(query, (start_year, country))
        return cursor.fetchall()
        
    except Exception as e:
        print("Something went wrong when executing the query: ", e)
        return None
        

def connect():
    #Copied from moodle
    try:
        connection = ps.connect(database=config.database, user=config.user, password=config.password, host="localhost")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection