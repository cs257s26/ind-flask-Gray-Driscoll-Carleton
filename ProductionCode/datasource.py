import psycopg2 as ps
import psqlconfig as config

def connect():
    #Copied from moodle
    try:
        connection = ps.connect(database=config.database, user=config.user, password=config.password, host="localhost")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection

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
                    WHERE (year = %s OR year = %s) AND country = %s
                    GROUP BY year;
                    """
            cursor.execute(query, (start_year, end_year, country))
            return cursor.fetchall()
    
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

def five_year_global_education_comparison(connection, start_year, country):
        try:
            cursor = connection.cursor()
            #returns the year, average years of education, and the global average years of education (gemini's use)
            query = """
                SELECT 
                    year, 
                    entity,
                    avg_years_education,
                    (SELECT AVG(avg_years_education) FROM education_data WHERE year = e.year) 
                    FROM education_data e
                    WHERE entity= %s AND year IN (%s, %s, %s, %s, %s);
                    """
            cursor.execute(query, (country, start_year, start_year + 1, start_year + 2, start_year + 3, start_year + 4))
            return cursor.fetchall()
    
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

#copied from moodle
def main():
    connection = connect()
    results = lit_over_time_country(connection, 1950, 2000, 'Canada')
    
    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)
    connection.close()

main()