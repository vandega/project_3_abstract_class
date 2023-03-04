from animal import Animal


class Dog(Animal):
    def __init__(self, name, age, breed, gender, its_can_fly=False, leg_count=4):
        super().__init__(name, age, leg_count)
        self._breed = breed
        self._gender = gender
        self._its_can_fly = its_can_fly

    def to_string(self):
        return {'name': self.get_name(), 'age': self.get_age(), 'breed': self._breed, 'gender': self._gender,
                'leg_count': self.get_leg_count(), 'can_fly': self.can_fly()}

    def communicate(self):
        return f"I'm {self.get_name()}, I'm dog and i can bark"

    def can_fly(self):
        if self._its_can_fly == True:
            return 'imposible'
        return False

