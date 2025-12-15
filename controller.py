from psycopg import errors

from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_main_menu()
            if choice == "1":
                self.handle_trip_menu()
            elif choice == "2":
                self.handle_client_menu()
            elif choice == "3":
                self.handle_payment_menu()
            elif choice == "0":
                break
            else:
                self.view.show_error("Невірно.")

    def handle_trip_menu(self):
        action = self.view.show_trip_menu()
        if action == "1":
            self.add_trip()
        elif action == "2":
            self.delete_trip()
        elif action == "3":
            self.list_trips()
        else:
            self.view.show_error("Невірно.")

    def list_trips(self):
        trips = self.model.trip_list()
        self.view.show_trips(trips)

    def add_trip(self):
        title, description, country, price_str = self.view.get_trip_input()
        try:
            price = float(price_str)
        except ValueError:
            self.view.show_error("Ціна має бути числом.")
            return

        try:
            self.model.trip_add(title, description, country, price)
            self.view.show_message("Додано")
        except Exception as e:
            self.view.show_error(e)

    def delete_trip(self):
        id_str = self.view.get_trip_id()
        try:
            trip_id = int(id_str)
        except ValueError:
            self.view.show_error("ID має бути числом.")
            return

        try:
            self.model.trip_delete(trip_id)
            self.view.show_message("Видалено")
        except errors.ForeignKeyViolation:
            self.view.show_error("Неможливо видалити: є залежні booking.")
            bookings = self.model.bookings_by_trip(trip_id)
            self.view.show_bookings(bookings)
        except Exception as e:
            self.view.show_error(e)
        
    def handle_client_menu(self):
        action = self.view.show_client_menu()
        if action == "1":
            self.add_client()
        elif action == "2":
            self.delete_client()
        elif action == "3":
            self.list_clients()
        else:
            self.view.show_error("Невірно.")

    def list_clients(self):
        clients = self.model.client_list()
        self.view.show_clients(clients)

    def add_client(self):
        name, email, phone, dob = self.view.get_client_input()
        try:
            self.model.client_add(name, email, phone, dob)
            self.view.show_message("Додано")
        except Exception as e:
            self.view.show_error(e)

    def delete_client(self):
        id_str = self.view.get_client_id()
        try:
            client_id = int(id_str)
        except ValueError:
            self.view.show_error("ID має бути числом.")
            return

        try:
            self.model.client_delete(client_id)
            self.view.show_message("Видалено")
        except errors.ForeignKeyViolation:
            self.view.show_error("Неможливо видалити: є залежні booking.")
            bookings = self.model.bookings_by_client(client_id)
            self.view.show_bookings(bookings)
        except Exception as e:
            self.view.show_error(e)

    def handle_payment_menu(self):
        action = self.view.show_payment_menu()
        if action == "1":
            self.add_payment()
        elif action == "2":
            self.delete_payment()
        elif action == "3":
            self.list_payments()
        else:
            self.view.show_error("Невірно.")

    def list_payments(self):
        payments = self.model.payment_list()
        self.view.show_payments(payments)

    def add_payment(self):
        booking_id_str, amount_str, method, discount_str = self.view.get_payment_input()

        try:
            booking_id = int(booking_id_str)
            amount = float(amount_str)
            discount = float(discount_str)
        except ValueError:
            self.view.show_error("booking_id, сума і знижка мають бути числами.")
            return

        try:
            self.model.payment_add(booking_id, amount, method, discount)
            self.view.show_message("Платіж успішно додано.")
        except ValueError as e:
            self.view.show_error(e)
        except errors.ForeignKeyViolation:
            self.view.show_error("Немає такого booking_id — вставка неможлива.")
        except Exception as e:
            self.view.show_error(e)

    def delete_payment(self):
        booking_id_str = self.view.get_payment_booking_id_for_delete()
        try:
            booking_id = int(booking_id_str)
        except ValueError:
            self.view.show_error("booking_id має бути числом.")
            return

        try:
            self.model.payment_delete(booking_id)
            self.view.show_message("Видалено")
        except Exception as e:
            self.view.show_error(e)
