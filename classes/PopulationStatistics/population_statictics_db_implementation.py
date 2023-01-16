from classes.User.user_db_implementation import get_all


def get_population_statistic():
    users = get_all()
    average_height = 0
    average_weight = 0
    for user in users:
        average_height += user.height
        average_weight += user.weight

    if average_weight != 0:
        average_weight /= len(users)
    if average_height != 0:
        average_height /= len(users)

    stat_touple = (average_height, average_weight)

    return stat_touple