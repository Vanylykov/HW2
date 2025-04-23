import sys

class Student:
    amount_of_students = 0

    def __init__(self, name="Марті МакФлай", height=None):
        self.height = height if height in range(1, 1001) else None
        self.name = name
        self.happiness = 50
        self.knowledge = 0
        self.age = 18

        if self.height:
            print("Я живий")
            print("Мене звати:", self)
        elif self.height is None:
            print("Я мертвий")
            print("Ви програли :( ")
            sys.exit()

        Student.amount_of_students += 1

    def print_height(self):
        print(f"Я студент і мій зріст {self.height} см")

    def grow(self, height):
        self.height += height

    def study(self, hours):
        self.knowledge += hours * 2
        self.happiness -= hours * 2
        print(f"{self.name} навчався {hours} годин. Знання: {self.knowledge}, Радість: {self.happiness}")

        if self.happiness <= 0:
            print("Ти став надто нещасним. Ти мертвий!")
            sys.exit()

        if self.knowledge >= 1000:
            print(f"Вітаємо! {self.name} випустився з університету!")
            sys.exit()

    def relax(self, hours):
        self.happiness += hours * 3
        self.knowledge -= hours * 1.5
        print(f"{self.name} відпочивав {hours} годин. Радість: {self.happiness}, Знання: {self.knowledge}")

        if self.happiness <= 0:
            print("Ти став надто нещасним. Ти мертвий!")
            sys.exit()

    def pass_time(self, days):
        self.age += days / 365
        self.happiness += days * 0.1  # Радість збільшується з часом
        self.knowledge += days * 0.05  # Знання трохи збільшуються з часом

        print(f"Пройшло {days} днів. Вік: {self.age:.2f} років, Радість: {self.happiness:.2f}, Знання: {self.knowledge:.2f}")

        if self.happiness <= 0:
            print("Ти став надто нещасним. Ти мертвий!")
            sys.exit()

        if self.knowledge >= 1000:
            print(f"Вітаємо! {self.name} випустився з університету!")
            sys.exit()

    def status(self):
        print(
            f"{self.name} - Вік: {self.age:.2f} років, Зріст: {self.height} см, Знання: {self.knowledge:.2f}, Радість: {self.happiness:.2f}")

    def __str__(self):
        return f"Я студент на ім'я {self.name}, мені {self.age:.2f} років, зріст {self.height} см, знання {self.knowledge:.2f}, радість {self.happiness:.2f}"


def student_simulation():
    student = Student(name=input("Введіть ім'я студента: "), height=int(input("Введіть зріст студента: ")))

    while True:
        print("\nОберіть дію:")
        print("1. Навчатися")
        print("2. Відпочивати")
        print("3. Показати статус")
        print("4. Пропустити час (дні)")
        print("5. Вийти")

        choice = input("Введіть свій вибір: ")

        if choice == "1":
            hours = int(input("Введіть кількість годин навчання: "))
            student.study(hours)
        elif choice == "2":
            hours = int(input("Введіть кількість годин відпочинку: "))
            student.relax(hours)
        elif choice == "3":
            student.status()
        elif choice == "4":
            days = int(input("Скільки днів пропустити? "))
            student.pass_time(days)
        elif choice == "5":
            print("Вихід із симуляції...")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


student_simulation()


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"На рахунок {self.account_number} внесено {amount} грн. Новий баланс: {self.balance} грн.")
        else:
            print("Сума для поповнення повинна бути більшою за нуль.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"З рахунку {self.account_number} знято {amount} грн. Новий баланс: {self.balance} грн.")
            else:
                print(f"Недостатньо коштів на рахунку {self.account_number}. Поточний баланс: {self.balance} грн.")
        else:
            print("Сума для зняття повинна бути більшою за нуль.")

# Приклад використання класу BankAccount
account1 = BankAccount("1234567890", 1000)
account2 = BankAccount("0987654321")

account1.deposit(500)
account2.deposit(100)

account1.withdraw(200)
account2.withdraw(150)

account1.withdraw(2000)