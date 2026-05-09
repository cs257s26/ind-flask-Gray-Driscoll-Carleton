from flask import Flask
from ProductionCode.command_line import load_data, get_country_average_year_schooling, get_country_literacy_growth, recent_high_low_cats

app = Flask(__name__)
load_data()

@app.route('/avgSchooling/<category>')
def get_avg_school_data(category):
    result = get_country_average_year_schooling(category)
    return result

@app.route('/litGrowth/<category>')
def get_lit_growth_data(category):
    result = get_country_literacy_growth(category)
    return result

if __name__ == '__main__':
    app.run(debug=True)