import random
import string


class Robot(object):
    used_name = []

    def __init__(self):
        self.name = ''
        self.reset()

    def generate_name(self):
        while True:
            name = ""
            name += "".join(random.sample(string.ascii_uppercase, 2))
            name += "".join(list(map(lambda x: str(x), random.sample(range(0, 9), 3))))

            if name not in self.used_name:
                self.used_name.append(name)
                return name

    def reset(self):
        self.name = self.generate_name()
