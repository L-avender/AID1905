class Animial:
    def __init__(self,pig_number,chicken_number,sheep_number):
        self.pig_number=pig_number
        self.chicken_number=chicken_number
        self.sheep_number=sheep_number

    def count_legs(self):
        total_legs =  self.pig_number* 4 +  self.chicken_number* 2 + self.sheep_number* 4
        return total_legs


from month01.skill_system.skill_manager import *
judge_zodiac(1994)