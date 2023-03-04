from animal import Animal


class Cat(Animal):
    def __init__(self, name, age, gender, breed, leg_count=4):
        super().__init__(name, age, leg_count)
        self._gender = gender
        self._breed = breed

    def to_string(self):
        return {'name': self.get_name(), 'age': self.get_age(), 'breed': self._breed, 'gender': self._gender,
                'leg_count': self.get_leg_count(), 'can_fly': self.can_fly()}

    def communicate(self):
        return 'cat say "miaw"'

    def can_fly(self):
        return False
