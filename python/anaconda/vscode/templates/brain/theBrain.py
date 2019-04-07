class Brain():
    pass

class TheRobot():
    train = Brain()
    train.x = 69
    train.y = 0

human = TheRobot()

print(human.train.x)