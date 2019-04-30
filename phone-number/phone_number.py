import re


class Phone(object):
    def __init__(self, phone_number):
        self.number = re.sub("[^0-9]", "", phone_number)
        if len(self.number) == 11 and self.number[0] != "1":
            raise ValueError("Invalid format")
        if len(self.number) == 11 and self.number[0] == "1":
            self.number = self.number[1:]
        if len(self.number) > 11 or len(self.number) < 9:
            raise ValueError("Invalid format")
        if int(self.number[0]) < 2 or int(self.number[3]) < 2:
            raise ValueError("Invalid format")
        self.area_code = self.number[0:3]

    def pretty(self):
        return "(" + self.number[0:3] + ")" + " " + self.number[3:6] + "-" + self.number[6:]

