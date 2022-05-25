from datetime import date


class Customer:
    def __init__(self, id: str, name: str, age: int, address: str):
        self.id = id
        self.name = name
        self.age = age
        self.address = address

    @classmethod
    def create_customer_from_birth(cls, _id, name, year, address):
        return cls(_id, name, date.today().year - year, address)