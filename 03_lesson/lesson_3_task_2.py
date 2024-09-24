from smartphone import Smartphone
catalog = [
    Smartphone("Samsung", "Galaxy", "+79123456789"),
    Smartphone("IPhone", "Pro", "+79234567890"),
    Smartphone("Infinix", "HOT", "+79345678901"),
    Smartphone("Huawei", "nova", "+79456789012"),
    Smartphone("Xiaomi", "Redmi", "+79567890123")
]

for smartphone in catalog:
    smartphone.info()
