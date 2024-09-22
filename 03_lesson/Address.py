class Address:
    def __init__(self, index, city, street, home, flat):
        self.index = index
        self.city = city
        self.street = street
        self.home = home
        self.flat = flat

    def __str__(self):
        return f"{self.index},{
            self.city},{self.street},{self.home},{self.flat}"
