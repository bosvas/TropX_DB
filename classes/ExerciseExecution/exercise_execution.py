import datetime
from dataclasses import dataclass, field
from classes.User import user
from classes.ExerciseSpecification import exercise_specification


@dataclass(order=True)
class ExerciseExecution:
    this_exercise_id: int = field()
    exercise: exercise_specification = field()
    user: user = field()
    date: datetime = field()
    repetitions: int = field()
    dumbbell_weight: int = field()

