from dataclasses import dataclass
from itertools import product
from random import choice

from faker import Faker

fake = Faker("ru_RU")
fake_eng = Faker("en_US")


# Faker.seed(0)
@dataclass
class Color:
    colors_list: list

    @staticmethod
    def generate_data():
        yield Color(
            colors_list=["red", "Blue", "Green", "yellow", "Purple", "black", "White", "voilet", "Indigo", "Magenta",
                         "aqua"]
        )


time_15min_step = [f"{h:02d}:{m:02d}" for h, m in product(range(24), range(0, 60, 15))]


@dataclass
class Date_and_Time:
    year: str
    month: str
    day: str
    time: str

    @staticmethod
    def generate_date_and_time():
        yield Date_and_Time(
            year=fake_eng.year(),
            month=fake_eng.month_name(),
            day=fake_eng.day_of_month(),
            time=choice(time_15min_step)
        )


@dataclass
class Group_Option:
    options_list: list

    @staticmethod
    def generate_group_option():
        yield Group_Option(
            options_list=["Group 1, option 1", "Group 1, option 2", "Group 2, option 1", "Group 2, option 2",
                          "A root option", "Another root option"]
        )
