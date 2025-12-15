from sqlalchemy import (
    create_engine, Column, Integer, BigInteger, String,
    Date, ForeignKey, Numeric
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "postgresql+psycopg://postgres:123@localhost:5432/postgres"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Trip(Base):
    __tablename__ = "trip"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    country_code = Column(String(3))
    price = Column(Numeric(12, 2))

    bookings = relationship("Booking", back_populates="trip", cascade="all, delete")

    def __repr__(self):
        return f"Trip(id={self.id}, title='{self.title}', country='{self.country_code}', price={self.price})"


class Client(Base):
    __tablename__ = "client"

    id = Column(BigInteger, primary_key=True)
    full_name = Column(String(128))
    email = Column(String(128))
    phone_number = Column(String(32))
    date_of_birth = Column(Date)

    bookings = relationship("Booking", back_populates="client", cascade="all, delete")

    def __repr__(self):
        return f"Client(id={self.id}, name='{self.full_name}', email='{self.email}')"


class Booking(Base):
    __tablename__ = "booking"

    id = Column(BigInteger, primary_key=True)
    client_id = Column(BigInteger, ForeignKey("client.id"))
    trip_id = Column(Integer, ForeignKey("trip.id"))
    date = Column(Date)
    status = Column(String(128))

    client = relationship("Client", back_populates="bookings")
    trip = relationship("Trip", back_populates="bookings")
    payment = relationship("Payment", back_populates="booking", uselist=False, cascade="all, delete")

    def __repr__(self):
        return f"Booking(id={self.id}, client_id={self.client_id}, trip_id={self.trip_id}, status='{self.status}')"


class Payment(Base):
    __tablename__ = "payment"

    booking_id = Column(Integer, ForeignKey("booking.id"), primary_key=True)
    amount = Column(Numeric(12, 2))
    method = Column(String(64))
    discount = Column(Numeric(5, 2))

    booking = relationship("Booking", back_populates="payment")

    def __repr__(self):
        return f"Payment(booking_id={self.booking_id}, amount={self.amount}, method='{self.method}', discount={self.discount})"
