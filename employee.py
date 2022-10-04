"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=0, hours=-1, bonus=0, bonus_count=-1):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.bonus = bonus
        self.bonus_count = bonus_count

    def get_pay(self):
        pay = 0
        if self.hours != -1:
            pay += self.hours * self.salary
        else:
            pay += self.salary
        if self.bonus != 0:
            if self.bonus_count != -1:
                pay += self.bonus_count * self.bonus
            else:
                pay += self.bonus
        return pay

    def __str__(self):
        output = f'{self.name} works on a '
        if self.hours != -1:
            output += f'contract of {self.hours} hours at {self.salary}/hour'
        else:
            output += f'monthly salary of {self.salary}'
        if self.bonus != 0:
            output += f' and receives a bonus commission '
            if self.bonus_count != -1:
                output += f'for {self.bonus_count} contract(s) at {self.bonus}/contract.'
            else:
                output += f'of {self.bonus}.'
        else:
            output += '.'
        output += f' Their total pay is {self.get_pay()}.'
        return output


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', salary=25, hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, bonus=200, bonus_count=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', salary=25, hours=150, bonus=220, bonus_count=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', salary=30, hours=120, bonus=600)

print(billie.get_pay())
print(str(billie))
print(charlie.get_pay())
print(str(charlie))
print(renee.get_pay())
print(str(renee))
print(jan.get_pay())
print(str(jan))
print(robbie.get_pay())
print(str(robbie))
print(ariel.get_pay())
print(str(ariel))
