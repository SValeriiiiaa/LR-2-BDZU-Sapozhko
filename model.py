# model.py
from sqlalchemy.orm import Session
from orm_base import SessionLocal, Trip, Client, Booking, Payment


class Model:

    # ---------------- TRIP ------------------

    def trip_list(self):
        with SessionLocal() as session:
            return session.query(Trip).all()

    def trip_add(self, title, description, country, price):
        with SessionLocal() as session:
            obj = Trip(
                title=title,
                description=description,
                country_code=country,
                price=price
            )
            session.add(obj)
            session.commit()

    def trip_delete(self, id_):
        with SessionLocal() as session:
            obj = session.get(Trip, id_)
            if obj:
                session.delete(obj)
                session.commit()

    def bookings_by_trip(self, trip_id):
        with SessionLocal() as session:
            return (
                session.query(Booking)
                .filter(Booking.trip_id == trip_id)
                .all()
            )

    # ---------------- CLIENT ------------------

    def client_list(self):
        with SessionLocal() as session:
            return session.query(Client).all()

    def client_add(self, name, email, phone, dob):
        with SessionLocal() as session:
            obj = Client(
                full_name=name,
                email=email,
                phone_number=phone,
                date_of_birth=dob
            )
            session.add(obj)
            session.commit()

    def client_delete(self, id_):
        with SessionLocal() as session:
            obj = session.get(Client, id_)
            if obj:
                session.delete(obj)
                session.commit()

    def bookings_by_client(self, client_id):
        with SessionLocal() as session:
            return (
                session.query(Booking)
                .filter(Booking.client_id == client_id)
                .all()
            )

    # ---------------- PAYMENT ------------------

    def payment_list(self):
        with SessionLocal() as session:
            return session.query(Payment).all()

    def payment_add(self, booking_id, amount, method, discount):
        with SessionLocal() as session:
            booking = session.get(Booking, booking_id)

            if booking is None:
                raise ValueError(f"Бронювання ID={booking_id} не існує.")

            # booking → payment — зв’язок 1:1  
            # Якщо payment вже існує — не додаємо дублікати
            if booking.payment:
                raise ValueError("Для цього booking платіж вже існує.")

            obj = Payment(
                booking_id=booking_id,
                amount=amount,
                method=method,
                discount=discount
            )
            session.add(obj)
            session.commit()

    def payment_delete(self, booking_id):
        with SessionLocal() as session:
            obj = session.get(Payment, booking_id)
            if obj:
                session.delete(obj)
                session.commit()
