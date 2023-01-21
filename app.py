from flask import Flask, redirect
from dotenv import load_dotenv
from classes.UserProfile import user_profiles_routes
from classes.PopulationStatistics import population_statistics_routes
from classes.User import user_routes
from classes.ExerciseSpecification import exercise_specification_routes
from classes.ExerciseExecution import exercise_execution_routes
from classes.MedicalInformation import medical_information_routes

load_dotenv()

app = Flask(__name__)
app.register_blueprint(user_profiles_routes.user_profiles_bp)
app.register_blueprint(population_statistics_routes.population_statistics_bp)
app.register_blueprint(user_routes.user_bp)
app.register_blueprint(exercise_specification_routes.exercise_specification_bp)
app.register_blueprint(exercise_execution_routes.exercise_execution_bp)
app.register_blueprint(medical_information_routes.midical_bp)


@app.route('/')
def index():
    return redirect('/tropx/userprofile/new')


if __name__ == '__main__':
    app.run(debug=True, port=5002)
