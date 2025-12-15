class View:

    def show_main_menu(self):
        print("""
            1) TRIP    1-додати 2-видалити 3-список
            2) CLIENT  1-додати 2-видалити 3-список
            3) PAYMENT 1-додати 2-видалити 3-список
            0) Вихід
            """)
        return input("Меню: ").strip()

    def show_trip_menu(self):
        return input("TRIP> ").strip()

    def show_client_menu(self):
        return input("CLIENT> ").strip()

    def show_payment_menu(self):
        return input("PAYMENT> ").strip()


    def get_trip_input(self):
        title = input("Назва: ")
        description = input("Опис: ")
        country = input("Код країни: ").upper()
        price = input("Ціна: ")
        return title, description, country, price

    def get_trip_id(self):
        return input("ID для видалення: ")

    def show_trips(self, trips):
        for r in trips:
            print(r)

    def get_client_input(self):
        name = input("ПІБ: ")
        email = input("Email: ")
        phone = input("Телефон: ")
        dob = input("Дата народження (YYYY-MM-DD): ")
        return name, email, phone, dob

    def get_client_id(self):
        return input("ID для видалення: ")

    def show_clients(self, clients):
        for r in clients:
            print(r)

    def get_payment_input(self):
        booking_id = input("booking_id (має існувати): ")
        amount = input("Сума: ")
        method = input("Метод: ")
        discount = input("Знижка: ")
        return booking_id, amount, method, discount

    def get_payment_booking_id_for_delete(self):
        return input("booking_id для видалення: ")

    def show_payments(self, payments):
        for r in payments:
            print(r)

    def show_bookings(self, bookings):
        for r in bookings:
            print("   ", r)

    def show_message(self, msg):
        print(msg)

    def show_error(self, msg):
        print("[ERR]", msg)
