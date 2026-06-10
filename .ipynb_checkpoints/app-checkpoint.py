import sys
import psycopg2 as ps
from flask import Flask
from ProductionCode import psqlconfig
from ProductionCode.datasource import lit_over_time_country, education_query

app = Flask(__name__)

def connect():
    #Copied from moodle
    try:
        connection = ps.connect(database=psqlconfig.database, user=psqlconfig.user, password=psqlconfig.password, host="localhost")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection

connection = connect()

@app.route('/litGrowth/<start_year>/<end_year>/<country>')
def get_lit_growth_data(start_year, end_year, country):
    result = lit_over_time_country(connection, start_year, end_year, country)
    return result

@app.route('/education/<country>/<start_year>')
def education_time_place(country, start_year):
    result = education_query(connection, country, start_year)
    return result


if __name__ == '__main__':
   app.run(port=int(sys.argv[1]), host = "stearns.mathcs.carleton.edu")