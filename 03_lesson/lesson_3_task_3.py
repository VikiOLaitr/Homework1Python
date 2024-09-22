from Address import Address
from Mailing import Mailing

to_address = Address("654398", "Севастополь", "Ленина", "12", "57")
from_address = Address("654321", "Симферополь", "Сталиграда пр.", "9", "6")

mailing = Mailing(to_address, from_address, 300, "DS09876")

print(mailing)
