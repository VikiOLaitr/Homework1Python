from Address import Address


class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = int(cost)
        self.track = track

    def get_track(self):
        return self.track

    def get_coast(self):
        return self.cost

