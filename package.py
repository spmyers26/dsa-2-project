# package.py

class Package:
    def __init__(self, package_id, address, city, zip_code, deadline, weight, load_time=None, delivery_time=None):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.load_time = load_time
        self.delivery_time = delivery_time

    def status(self, time):
        if self.load_time is None:
            return 'is at hub'
        if self.delivery_time is None:
            return 'is en route'
        if self.delivery_time < time:
            return f'was delivered at {self.delivery_time}'
        elif self.load_time < time:
            return 'is en route'
        else:
            return 'is at hub'

    def __str__(self, time):
        return f'Package {self.package_id} {self.status(time)}'
