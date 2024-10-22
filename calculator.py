#Basic Calculator

class Calculate:
    def __init__(self, first_number: int, operator: str, second_number: int):
        self.first_number = first_number
        self.operator = operator
        self.second_number = second_number
        self.result: int = eval(f"{self.first_number} {self.operator} {self.second_number}")

calc_instance = Calculate(2, "/", 3)

print (calc_instance.result)