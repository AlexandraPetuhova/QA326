# # задача Реализуйте класс для управления системой бронирования отелей. Класс Бронь должен содержать информацию о
# # госте, дате заезда и выезда, типе номера. *(необязательно) Методы должны позволять бронировать, отменять бронь и
# # проверять доступность номеров на определенные даты.


from datetime import date


reservation_database = []


class Reservation:
    def __init__(self, guest_name: str, check_in_date: date, check_out_date: date, room_type: str):
        self.id = None
        self.guest_name = guest_name
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room_type = room_type

    def __repr__(self):
        return f"Name: {self.guest_name}\nCheck-in date: {self.check_in_date}\nCheck-out date: {self.check_out_date}\nRoom type: {self.room_type}\nID: {self.id}\n"

    def make_reservation(self):
        try:
            self.id = reservation_database[-1].id + 1
        except:
            self.id = 1
        reservation_database.append(self)
        print(f"Reservation for {self.guest_name} created successfully.")

    def remove_reservation(self):
        for reservation in reservation_database:
            if reservation.id == self.id:
                reservation_database.remove(reservation)
                print(f"Reservation for {self.guest_name} removed successfully.")

    def date_check(self):
        available = True
        for reservation in reservation_database:
            if self.room_type == reservation.room_type:
                if self.check_in_date > reservation.check_out_date or self.check_out_date < reservation.check_in_date:
                    pass
                else:
                    print(f"{self.guest_name}, the room is not available for these dates.")
                    available = False
                    break
            else:
                pass
        return available


guest1 = Reservation("Lena", "2024-06-11", "2024-06-18", "lux")
guest2 = Reservation("Vova", "2024-07-01", "2024-07-04", "standard")
guest3 = Reservation("Ivan", "2024-06-17", "2024-06-30", "economy")
guest4 = Reservation("Anna", "2024-06-04", "2024-06-18", "economy")

guest1.make_reservation()
if guest2.date_check():
    guest2.make_reservation()
if guest3.date_check():
    guest3.make_reservation()
guest1.remove_reservation()
guest1.make_reservation()
if guest4.date_check():
    guest4.make_reservation()


for guest in reservation_database:
    print(guest)

# # задача Класс Книга должен содержать информацию о названии, авторе и жанре книги. Метод show должен показать
# # информацию об объекте. Создайте два разных объекта и вызовите у них метод show
#
# class Book:
#     def __init__(self, title: str, author: str, genre: str):
#         self.title = title
#         self.author = author
#         self.genre = genre
#
#     def show(self):
#         return f"title: {self.title}\nauthor: {self.author}\ngenre: {self.genre}\n"
#
#
# harry_potter = Book("Harry Potter", "Joan K. Rowling", "fantasy")
# witcher = Book("Witcher", "A. Sapkovsky", "fantasy")
# print(harry_potter.show(), witcher.show(), sep='\n')
#
#
# # задача
# # Класс БанковскийАккаунт должен хранить информацию о владельце, балансе
# # Метод show должен показать информацию об объекте. Создайте два разных объекта и вызовите у них метод show
#
# class Bank_account:
#
#     def __init__(self, name: str, balance: int = 0):
#         self.name = name
#         self.balance = balance
#
#     def __repr__(self):
#         return f"name: {self.name}\nbalance: {self.balance}\n"
#
#     def add_money(self, sum):
#         self.balance += sum
#
#     def withdraw_money(self, sum):
#         if self.balance >= sum:
#             self.balance -= sum
#         else:
#             print("Operation denied\n")
#
#
# jack = Bank_account("Jack", 300)
# daniel = Bank_account("Daniel", 500)
#
# jack.withdraw_money(450)
# daniel.add_money(1000)
#
# print(jack, daniel, sep="\n")
