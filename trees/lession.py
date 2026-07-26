# class Car:
#     def __init__(self,brand, model , year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def display_info(self):
#         print("brand:", self.brand)
#         print("model:", self.model)
#         print("year:", self.year)
# c1 = Car("Toyota", "Camry", 2020)
# c1.display_info()

# class Student:
#     def __init__ (self,name,grade):
#         self.name = name
#         self.__grade = grade
#     def study(self,hours):
#         self.__grade += hours * 2
#         if self.__grade > 20:
#             self.__grade = 20
#     def show_grade(self):
#         print(self.__grade)
# s1 = Student("toufik",16)
# s1.study(3)
# # print(s1._Student__grade)
# print(s1.__dict__)

# class Phone:
#     def __init__ (self, brand, battery):
#         self.brand = brand
#         self.__battery = battery

#     def charge(self, percent):
#         self.__battery += percent
#         if self.__battery > 100:
#             self.__battery = 100
#     def use(self, percent):
#         self.__battery -= percent
#         if self.__battery < 0:
#             self.__battery = 0
#     def show_battery(self):
#         print(self.__battery)

#     def battery_percentage(self):
#         return self.__battery


# phone = Phone("Samsung", 50)

# # phone.charge(30)
# phone.charge(50)

# phone.show_battery()
# print(phone.battery_percentage())

from copy import deepcopy


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        self.__history = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__history.append(("deposit", amount))
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                self.__history.append(("withdraw", amount))
            else:
                print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

    def transfer(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            print("Invalid account.")
            return
        self.withdraw(amount)
        other_account.deposit(amount)
        other_account.__history.append(("receive", amount, self.owner))
        self.__history.append(("transfer", amount, other_account.owner))
        print("Transfer failed")

    def show_history(self):
        return deepcopy(self.__history)


account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)
account1.transfer(account2, 200)
print(account1.show_history())
print(account2.show_history())
