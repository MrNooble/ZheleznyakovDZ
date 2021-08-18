class Worker:
    def __int__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_profit(self):
        return f'{sum(self._income.values())}'


meneger = Position('Sviat', "Zel", 'CEO', 50000000, 12000000)
print(meneger.get_full_name())
print(meneger.position)
print(meneger.get_full_profit())
