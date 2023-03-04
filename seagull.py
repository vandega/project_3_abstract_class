from animal import Animal


class Seagull(Animal):
    def __init__(self, name, age, gender, leg_count=2):
        super().__init__(name, age, leg_count)
        self._gender = gender
    def to_string(self):
        return {'name': self.get_name(), 'age': self.get_age(),
                'gender': self._gender, 'leg_count': self.get_leg_count(), 'can_fly': self.can_fly()}

    def communicate(self):
        return 'i dont  know hat seagull voice like'

    def can_fly(self):
        return  True