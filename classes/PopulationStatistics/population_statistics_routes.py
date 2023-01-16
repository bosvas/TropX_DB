from flask import Blueprint, render_template, request
from classes.PopulationStatistics import population_statictics_db_implementation


population_statistics_bp = Blueprint('population_statistics_bp', __name__)


@population_statistics_bp.route("/tropx/statistic")
def all_population_statistic():
    height, weight, total_exercises = population_statictics_db_implementation.get_population_statistic()
    return render_template('tropx/statistic/index.html', height=height, weight=weight, total_exercises=total_exercises)