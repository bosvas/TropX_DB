from classes.User import user_db_implementation
from classes.ExerciseSpecification import exercise_specification_db_implementation

def get_population_statistic():
    exercises = exercise_specification_db_implementation.get_all()
    total_exercises = len(exercises)

    users = user_db_implementation.get_all()
    average_height = 0
    average_weight = 0
    for user in users:
        average_height += user.height
        average_weight += user.weight

    if average_weight != 0:
        average_weight /= len(users)
    if average_height != 0:
        average_height /= len(users)

    stat_touple = (average_height, average_weight, total_exercises)

    return stat_touple