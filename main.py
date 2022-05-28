from inspect import Attribute


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        # pass
    def change_name(self, name):
        print(f"{name}")
    
    def change_age(self, age):
        print(f"{age}")

    def add_track(self, tracks):
        print((f"{self.tracks}")+ f"{tracks}")

    def get_score(self):
        print(f"{self.score}")

Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()