from abc import abstractmethod, ABC


class Animal(ABC):
    def __init__(self, name, age, leg_count):
        self._name = name
        self._age = age
        self._leg_count = leg_count

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_leg_count(self):
        return self._leg_count

    @abstractmethod
    def to_string(self):
        return 'no information'

    @abstractmethod
    def communicate(self):
        return "no infrmation"

    @abstractmethod
    def can_fly(self):
        return False
