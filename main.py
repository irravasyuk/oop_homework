# Завдання 3
# Створіть клас «Країна». Збережіть у класі: назву країни,
# назву континенту, кількість жителів країни, телефонний
# код країни, назву столиці, назву міст країни. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій.

class Country:
    def __init__(self, name, name_of_continent, pupulation, phone_code, capital, city_name):
        self.name = name
        self.name_of_continent = name_of_continent
        self.population = pupulation
        self.phone_code = phone_code
        self.capital = capital
        self.city_name = city_name

    def input_data(self):
        self.name = input("Введіть назву країни: ")
        self.name_of_continent = input("Введіть назву континенту: ")
        self.population = int(input("Введіть кількість жителів країни: "))
        self.phone_code = input("Введіть телефонний код країни: ")
        self.capital = input("Введіть столицю країни: ")
        cities = input("Введіть назви міст країни через кому: ")
        self.city_name = [city for city in cities.split(",")]

    def display(self):
        print("Назва країни: ", self.name)
        print("Назва континету: ", self.name_of_continent)
        print("Кількість жителів: ", self.population)
        print("Телефонний код країни: ", self.phone_code)
        print("Столиця країни: ", self.capital)
        print("Назви міст країни: ", ", ".join(self.city_name))

country1 = Country("", "", 0, "", "", [])
country1.input_data()
print("\nІнформація про країну: ")
country1.display()

