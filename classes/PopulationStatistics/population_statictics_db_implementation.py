from classes.User import user_db_implementation
from classes.ExerciseSpecification import exercise_specification_db_implementation
from classes.ExerciseExecution import exercise_execution_db_implementation

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

    executions = exercise_execution_db_implementation.get_all_executions()
    exercises_list=[]
    for exercise in exercises:
        i = 0
        mid_correct = 0
        mid_number = 0
        for execution in executions:
            if execution.exercise_id == exercise.exercise_id:
                mid_correct += execution.correct_rate
                mid_number += execution.number_of_repetitions
                i += 1

        if i!=0:
            mid_number /= i
            mid_correct /= i
            exercise_touple = (exercise.name, i,  round(mid_correct, 2), round(mid_number, 2))
            exercises_list.append(exercise_touple)


    stat_touple = (average_height, average_weight, total_exercises, exercises_list)

    return stat_touple