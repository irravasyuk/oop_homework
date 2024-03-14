# Завдання 2
# Створіть клас «Місто». Збережіть у класі: назву міста,
# назву регіону, назву країни, кількість жителів у місті,
# поштовий індекс міста, телефонний код міста. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій.

class City:
    def __init__(self, name, region, country, population, postal_code, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def input_data(self):
        self.name = input("Введіть назву міста: ")
        self.region = input("Введіть назву регіону: ")
        self.country = input("Введіть назву країни: ")
        self.population = input("Введіть кількість жителів у місті: ")
        self.postal_code = input("Введіть поштовий індекс міста: ")
        self.phone_code = input("Введіть телефонний код міста: ")

    def display(self):
        print("Назва міста: ", self.name)
        print("Назва регіону: ", self.region)
        print("Назва країни: ", self.country)
        print("Кількість жителів міста: ", self.population)
        print("Поштовий індекс міста: ", self.postal_code)
        print("Телефонний код міста: ", self.phone_code)

city1 = City("", "", "", 0, "", "")
city1.input_data()
print("\nІнформація про місто: ")
city1.display()