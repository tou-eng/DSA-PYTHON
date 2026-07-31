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




# from copy import deepcopy


# class BankAccount:

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#         self.__history = []

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             self.__history.append(("deposit", amount))
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > 0:
#             if self.__balance >= amount:
#                 self.__balance -= amount
#                 self.__history.append(("withdraw", amount))
#             else:
#                 print("Insufficient balance.")

#     def get_balance(self):
#         return self.__balance

#     def transfer(self, other_account, amount):
#         if not isinstance(other_account, BankAccount):
#             print("Invalid account.")
#             return
#         self.withdraw(amount)
#         other_account.deposit(amount)
#         other_account.__history.append(("receive", amount, self.owner))
#         self.__history.append(("transfer", amount, other_account.owner))
#         print("Transfer failed")

#     def show_history(self):
#         return deepcopy(self.__history)


# account1 = BankAccount("Alice", 1000)
# account2 = BankAccount("Bob", 500)
# account1.transfer(account2, 200)
# print(account1.show_history())
# print(account2.show_history())

#i am trying to solve this exercice
# class car:
#     def __init__(self, speed, fuel):
#         self.__speed = max(0, min(speed, 220))
#         self.__fuel = max(0, min(fuel, 50))
#     @property
#     def speed(self):
#         return self.__speed

#     @property
#     def fuel(self):
#         return self.__fuel

#     def accelerate(self, amount):
#         if self.__fuel > 0:
#             if amount <= 0:
#                 print("Amount must be positive.")
#                 return
#             self.__speed += amount
#             self.__fuel -= amount * 0.1
#         else:
#                 self.__fuel = 0
#                 print("Not enough fuel.")
#                 return self.__speed


#     def brake(self, amount):
#         self.__speed -= amount
#         if self.__speed < 0:
#             self.__speed = 0
#         return self.__speed

#     def refuel(self, liters):
#         if liters < 0:
#             print("Liters cannot be negative.")
#             return
#         self.__fuel += liters
#         if self.__fuel > 50:
#             self.__fuel = 50
#         return self.__fuel


#the right way to solve the exercice is this one
# class Car:
#     MAX_SPEED = 220
#     MAX_FUEL = 50

#     def __init__(self, speed=0, fuel=50):
#         self.__speed = max(0, min(speed, Car.MAX_SPEED))
#         self.__fuel = max(0, min(fuel, Car.MAX_FUEL))

#     # ---------- Read-only properties ----------
#     @property
#     def speed(self):
#         return self.__speed

#     @property
#     def fuel(self):
#         return self.__fuel

#     # ---------- Behaviors ----------
#     def accelerate(self, amount):
#         if amount <= 0:
#             print("Acceleration amount must be positive.")
#             return

#         if self.__fuel <= 0:
#             print("Not enough fuel.")
#             return

#         # Increase speed
#         self.__speed += amount
#         if self.__speed > Car.MAX_SPEED:
#             self.__speed = Car.MAX_SPEED

#         # Consume fuel
#         self.__fuel -= amount * 0.1
#         if self.__fuel < 0:
#             self.__fuel = 0

#     def brake(self, amount):
#         if amount <= 0:
#             print("Brake amount must be positive.")
#             return

#         self.__speed -= amount
#         if self.__speed < 0:
#             self.__speed = 0

#     def refuel(self, liters):
#         if liters <= 0:
#             print("Fuel amount must be positive.")
#             return

#         self.__fuel += liters
#         if self.__fuel > Car.MAX_FUEL:
#             self.__fuel = Car.MAX_FUEL

#     def show_status(self):
#         print(f"Speed: {self.__speed} km/h")
#         print(f"Fuel : {self.__fuel:.1f} L")


# car = Car(speed=30, fuel=10)

# car.show_status()

# car.accelerate(40)
# car.show_status()

# car.brake(20)
# car.show_status()

# car.refuel(30)
# car.show_status()

# class VideoGameCharacter:
#     def __init__(self, name):
#         self.__name=name
#         self.__health = 100
#         self.__mana = 100
#         self.__level = 1
#         self.__exp = 0

#     @property
#     def health(self):
#         return self.__health

#     @property
#     def mana(self):
#         return self.__mana

#     @property
#     def level(self):
#         return self.__level

#     @property
#     def exp(self):
#         return self.__exp

#     # ---------- Behaviors ----------
#     def take_damage(self, amount):
#         if amount>0:
#             self.__health -= amount
#             if self.__health<=0:
#                 print("DEAD")
#                 return

#     def heal(self, amount):
#         if self.__health > 0 :
#             if amount>0:
#                 self.__health += amount
#         else:
#             print("DEAD")
#             return

#     def cast_spell(self, cost):
#         if self.__mana>0:
#             if cost>0:
#                 self.__mana -= cost
#         else:
#             print("No mana to cast")
#             return

#     def gain_experience(self, xp):
#         self.__exp += xp
#         if self.__exp > 100:
#             self.__level += 1
#             self.__exp -= 100
#             self.__health = 100
#             self.__mana = 100
#     def show_status(self):
#         print(f"{self.__name}'s status")
#         print(f"health: {self.__health}")
#         print(f"mana: {self.__mana}")
#         print(f"level: {self.__level}")
#         print(f"experience: {self.__exp}")


# toufik = VideoGameCharacter(tau)
# toufik.gain_experience(12)
# toufik.show_status()


# #my try
# from copy import deepcopy


# class Item:
#     def __init__(self, name, price):
#         self.__name = name
#         self.__price = price

#     @property
#     def name(self):
#         return self.__name

#     @property
#     def price(self):
#         return self.__price

#     def __str__(self):
#         return f"{self.__name} - {self.__price} gold"
# class Inventory:
#     def __init__(self):
#         self.__items=[]
#     def add_item(self,item):
#         if not isinstance(item, Item):
#                 print("Invalid item.")
#                 return
#         self.__items.append(item)
#     def remove_item(self,item):
#         if not isinstance(item, Item):
#                 print("Invalid item.")
#                 return
#         self.__items.remove(item)
#     def show_items(self):
#         return deepcopy(self.__items)

# class Player:
#     def __init__(self,name):
#         self.__name=name
#         self.__inventory=Inventory()

#     def pick_item(self,item):
#         self.__inventory.add_item(item)

#     def drop_item(self,item):
#         self.__inventory.remove_item(item)

#     def show_inventory(self):
#         return self.__inventory.show_items()
# apple = Item("Golden Apple", 20)
# banana = Item("Golden Banana", 30)

# toufik = Player("Toufik")

# toufik.pick_item(apple)
# toufik.pick_item(banana)

# print(toufik.show_inventory())

# #correct solution is just must know __str__ and __repr__
# from copy import deepcopy


# class Item:
#     def __init__(self, name, price):
#         self.__name = name
#         self.__price = price

#     @property
#     def name(self):
#         return self.__name

#     @property
#     def price(self):
#         return self.__price

#     def __str__(self):
#         return f"{self.__name} - {self.__price} gold"

#     def __repr__(self):
#         return str(self)


# class Inventory:
#     def __init__(self):
#         self.__items = []

#     def add_item(self, item):
#         if not isinstance(item, Item):
#             print("Invalid item.")
#             return

#         self.__items.append(item)

#     def remove_item(self, item):
#         if not isinstance(item, Item):
#             print("Invalid item.")
#             return

#         if item not in self.__items:
#             print("Item not found.")
#             return

#         self.__items.remove(item)

#     def show_items(self):
#         return deepcopy(self.__items)


# class Player:
#     def __init__(self, name):
#         self.__name = name
#         self.__inventory = Inventory()

#     def pick_item(self, item):
#         self.__inventory.add_item(item)

#     def drop_item(self, item):
#         self.__inventory.remove_item(item)

#     def show_inventory(self):
#         return self.__inventory.show_items()


# # ---------------- Test ----------------

# apple = Item("Golden Apple", 20)
# banana = Item("Golden Banana", 30)

# toufik = Player("Toufik")

# toufik.pick_item(apple)
# toufik.pick_item(banana)

# print(toufik.show_inventory())


# class Character:
#     def __init__(self,name):
#         self.__name=name
#         self.__health=100
#         self.__exp=0
#         self.__level=1

#     @property
#     def health(self):
#         return self.__health
#     @property
#     def exp(self):
#         return self.__exp
#     @property
#     def level(self):
#         return self.__level
#     #     # ---------- Behaviors ----------
#     def take_damage(self, amount):
#         if amount>0:
#             self.__health -= amount
#             if self.__health<=0:
#                 print("DEAD")
#                 return

#     def heal(self, amount):
#         if self.__health > 0 :
#             if amount>0:
#                 self.__health += amount
#         else:
#             print("DEAD")
#             return

#     def gain_experience(self, xp):
#         self.__exp += xp
#         if self.__exp >= 100:
#             self.__level += 1
#             self.__exp -= 100
#             self.__health = 100

#     def show_status(self):
#         print(f"{self.__name}'s status")
#         print(f"Health: {self.__health}")
#         print(f"Level: {self.__level}")
#         print(f"Experience: {self.__exp}")


# class Mage(Character):
#     def __init__(self,name):
#         super().__init__(name)
#         self.__mana=100

#     @property
#     def mana(self):
#         return self.__mana
    
#     def cast_spell(self, cost):
#         if self.__mana>0:
#             if cost>0:
#                 self.__mana -= cost

#     def gain_experience(self, xp):
#         super().gain_experience(xp)
#         self.__mana = 100
#         # If the character leveled up,
#         # restore mana

#     def show_status(self):
#         super().show_status()
#         print(f"Mana: {self.__mana}")

# class Warrior(Character):
#     def __init__(self, name):
#         super().__init__(name)
#         self.__aura = 100


#     @property
#     def aura(self):
#         return self.__aura

#     def sowrd_art(self, cost):
#         if self.__aura > 0:
#             if cost > 0:
#                 self.__aura -= cost

#     def gain_experience(self, xp):
#         super().gain_experience(xp)
#         self.__aura = 100

#     def show_status(self):
#         super().show_status()
#         print(f"Aura: {self.__aura}")

#RPG game
# class Pet:
#     def __init__(self,name):
#         self.__name=name
#         self.__health=100
#     @property
#     def health(self):
#         return self.__health
#     def eat(self,food):
#         if food>0:
#             self.__health = min(100, self.__health + food)
#     def take_damage(self, amount):
#         if amount>0:
#             self.__health -= amount
#             if self.__health<=0:
#                 print("DEAD")
#                 return
#     def show_status(self):
#         print(f"{self.__name}'s status")
#         print(f"Health: {self.__health}")
# class Dog(Pet):
#     def __init__(self, name):
#         super().__init__(name)
#         self.__energy=100
#     def bark(self,cost):
#         if cost>0:
#             if self.__energy>0:
#                 self.__energy-=cost
#                 print("danger danger hoof hoof")
#             else:
#                 print("feed me feed me")

#     def eat(self, food):
#         super().eat(food)
#         self.__energy = min(100, self.__energy + food)
#     def show_status(self):
#         super().show_status()
#         print(f"Energy: {self.__energy}")
# class Dragon(Pet):
#     def __init__(self, name):
#         super().__init__(name)
#         self.__fire=100
#     def breath_fire(self,cost):
#         if cost>0:
#             if self.__fire>0:
#                 self.__fire-=cost
#                 print("FIIIIIIIIIIIIIRRRRREEEEEE")
#             else:
#                 print("feed me feed me")

#     def eat(self,food):
#         super().eat(food)
#         self.__fire = min(100, self.__fire + food)
#     def show_status(self):
#         super().show_status()
#         print(f"Fire: {self.__fire}")
# safira=Dragon("safira")
# safira.breath_fire(150)
# safira.show_status()

#school
# class Person:
#     def __init__(self,name, age):
#         self.__name=name
#         self.__age=age
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def age(self):
#         return self.__age

#     def introduce(self):
#         print(f"Hi, I'm {self.__name} and I'm {self.__age} years old.")

# class Student(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self.__grade=grade

#     @property
#     def grade(self):
#         return self.__grade
#     def introduce(self):
#         super().introduce()
#         print(f"Grade : {self.__grade}")
# s1=Student("toufik",26,20)
# s1.introduce()

#Bank account
# class Account:
#     def __init__(self, owner, balance):
#         self.__owner=owner
#         self._balance=balance

#     @property
#     def owner(self):
#         return self.__owner
#     @property
#     def balance(self):
#         return self._balance

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#         else:
#             print("Deposit amount must be positive.")
#     def withdraw(self, amount):
#         if amount > 0:
#             if self._balance >= amount:
#                 self._balance -= amount
#             else:
#                 print("Insufficient balance.")
#     def show_balance(self):
#         print(f"{self.__owner}'s balance is : {self._balance}")
# class SavingsAccount(Account):
#     def __init__(self, owner, balance):
#         super().__init__(owner, balance)
#         self.__interest_rate=0.05
#     @property
#     def interest(self):
#         return self.__interest_rate
#     def apply_interest(self):
#         self._balance+=self._balance*self.__interest_rate
#     def show_balance(self):
#         super().show_balance()
        
# class PremiumAccount(Account):
#     def __init__(self,owner, balance):
#         super().__init__(owner,balance)
#         self.__cashback_rate=0.05
#     @property
#     def cashback(self):
#         return self.__cashback_rate
#     def withdraw(self, amount):
#         super().withdraw(amount)
#         self._balance += amount * self.__cashback_rate
#     def show_balance(self):
#         super().show_balance()
# tou=PremiumAccount("toufik",20000)
# tou.withdraw(1)
# tou.show_balance()
# class Vehicle:
#     MAX_SPEED = 220
#     MAX_FUEL = 50

#     def __init__(self, speed, fuel, brand):
#         self._speed = max(0, min(speed, self.MAX_SPEED))
#         self._fuel = max(0, min(fuel, self.MAX_FUEL))
#         self._brand=brand
#     @property
#     def speed(self):
#         return self._speed
#     @property
#     def fuel(self):
#         return self._fuel
#     @property
#     def brand(self):
#         return self._brand
    
#     #     # ---------- Behaviors ----------
#     def accelerate(self, amount):
#         if amount <= 0:
#             print("Acceleration amount must be positive.")
#             return

#         if self._fuel <= 0:
#             print("Not enough fuel.")
#             return

#         # Increase speed
#         self._speed += amount
#         if self._speed > Vehicle.MAX_SPEED:
#             self._speed = Vehicle.MAX_SPEED

#         # Consume fuel
#         self._fuel -= amount * 0.1
#         if self._fuel < 0:
#             self._fuel = 0

#     def brake(self, amount):
#         if amount <= 0:
#             print("Brake amount must be positive.")
#             return

#         self._speed -= amount
#         if self._speed < 0:
#             self._speed = 0

#     def refuel(self, liters):
#         if liters <= 0:
#             print("Fuel amount must be positive.")
#             return

#         self._fuel += liters
#         if self._fuel > Vehicle.MAX_FUEL:
#             self._fuel = Vehicle.MAX_FUEL

#     def show_status(self):
#         print(f"Speed: {self._speed} km/h")
#         print(f"Fuel : {self._fuel:.1f} L")
#         print(f"Brand : {self._brand}")
# class Car(Vehicle):
#     MAX_SPEED = 260
#     MAX_FUEL = 65
#     def __init__(self, speed, fuel, brand, doors):
#         super().__init__(speed, fuel, brand)
#         self.__doors=doors
#     @property
#     def doors(self):
#         return self.__doors
#     def show_status(self):
#         super().show_status()
#         print(f"The number of Doors : {self.__doors}")
# class Motorcycle(Vehicle):
#     MAX_SPEED = 320
#     MAX_FUEL = 20
#     def __init__(self, speed, fuel, brand, helmet_required):
#         super().__init__(speed, fuel, brand)
#         self.__helmet_required=helmet_required
#     @property
#     def helmet_required(self):
#         return self.__helmet_required
#     def show_status(self):
#         super().show_status()
#         print(f"Helmet status : {self.__helmet_required}")
# class Truck(Vehicle):
#     MAX_SPEED = 140
#     MAX_FUEL = 180
#     def __init__(self, speed, fuel, brand, cargo_weight):
#         super().__init__(speed, fuel, brand)
#         self.__cargo_weight = cargo_weight
#     @property
#     def cargo_weight(self):
#         return self.__cargo_weight
#     def show_status(self):
#         super().show_status()
#         print(f"Cargo weight: {self.__cargo_weight} Kg")

# car1=Car(200,30,"tesla",2)
# truck1=Truck(60,70,"Super",3000)
# motor=Motorcycle(300,20,"vm","yes")
# car1.show_status()
# motor.show_status()
# truck1.show_status()
