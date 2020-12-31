"""
whenever the class object is called:
the instance is always passed as the 1st argument!

self -> always refer to a particular instance!

Ref - https://youtu.be/AsafkCAJpJ0?t=272
"""


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return f'{self.first} {self.last}'


a = Employee('Joseph', 'Yu')

print(a.full_name())

print(Employee('Corey', 'Schafer').full_name())
