import time
from datetime import datetime


class Place:
    """
    class Place is to describe the location of a class
    """

    def __init__(self, _building, _room):
        self.building = _building
        self.room = _room


class Class:
    """
    class Class is to describe a class
    """

    def __init__(self, _class_name, _teacher, _place, _time):
        self.class_name = _class_name
        self.teacher = _teacher
        self.place = _place
        self.time = _time

    def parse_ymd(s):
        year_s, mon_s, day_s = s.split('-')
        return datetime(int(year_s), int(mon_s), int(day_s))


class Day:
    """
    class Day is to describe a single day
    """

    def __init__(self, _class_list):
        self.class_list = _class_list



