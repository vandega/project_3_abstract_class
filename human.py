from animal import Animal


class Human(Animal):
    def __init__(self, name, age, gender, leg_count=2, its_can_fly=False):
        super().__init__(name, age, leg_count)
        self._gender = gender
        self._its_can_fly = its_can_fly
        if self._leg_count < 2:
            print('person injured')

    def to_string(self):
        return {'name': self.get_name(), 'age': self.get_age(), 'gender': self._gender,
                "leg_count": self.get_leg_count(), 'can_fly': self.can_fly()}

    def communicate(self):
        return f'hello im {self.get_name()}, im human and i can talk'

    def can_fly(self):
        if self._its_can_fly: return 'Jehovah'
        return False
