from human import Human
from dog import Dog
from cat import Cat
from seagull import Seagull

human1 = Human('peter', 25, "male")
dog1 = Dog('marley', 7, 'unknown', 'Male')
cat1 = Cat('burka', 2, 'female', 'egypt')
seagull1 = Seagull('dodo', 1, 'female')

a = [human1, dog1, cat1, seagull1]

for i in a:
    print(i.to_string())
