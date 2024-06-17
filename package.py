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
        if self.delivery_time[0] < time[0] or self.delivery_time[0] == time[0] and self.delivery_time[1] <= time[1]:
            hour = self.delivery_time[0]
            minute = self.delivery_time[1]
            am_or_pm = 'AM'
            zero_check = ''
            if hour > 12:
                hour = hour - 12
                am_or_pm = 'PM'
            if minute < 10:
                zero_check = '0'
            return f'was delivered. Delivery completed at {hour}:{zero_check}{minute} {am_or_pm}'
        elif self.load_time[0] < time[0] or self.load_time[0] == time[0] and self.load_time[1] <= time[1]:
            return 'was en route.'
        else:
            delayed_packages = [6, 25, 28, 32]
            if self.package_id in delayed_packages:
                return 'was delayed on flight.'
            return 'was at hub.'

    def __str__(self, time):
        return f'Package {self.package_id} {self.status(time)}'
