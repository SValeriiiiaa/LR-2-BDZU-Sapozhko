from orm_base import Base, engine

Base.metadata.create_all(engine)
print("ORM таблиці створено!")
