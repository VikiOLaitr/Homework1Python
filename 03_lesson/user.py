class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first(self):
        return self.first_name

    def get_last(self):
        return self.last_name

    def get_first_last(self):
        return f"Имя: {self.first_name}, Фамилия: {self.last_name}"
