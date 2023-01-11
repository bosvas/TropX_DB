import datetime
from dataclasses import dataclass, field
from classes.User import user


@dataclass(order=True)
class ExerciseSpecification:
    exercise_id: int = field()
    exercise_name: str = field()