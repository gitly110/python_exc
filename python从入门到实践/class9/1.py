from random import randint


class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        randomnum = randint(1, self.sides)
        print(randomnum, end='  ')


die6 = Die(6)
die6.roll_die()
for i in range(10):
    die6.roll_die()
