# truck

class Truck:
    def __init__(self):
        self.packages = []
        self.mileage = 0
        self.current_address = '4001 South 700 East'

    def deliver_packages(self, package_table, distances, load_time):
        while len(self.packages) > 0:
            # Get distance to first package in packages[]
            package_to_deliver = self.packages[0]
            next_address = package_table.search(self.packages[0]).address
            x = distances[0].index(self.current_address)
            y = distances[0].index(package_table.search(self.packages[0]).address)
            if distances[x][y] != '':
                mileage_to_next_address = float(distances[x][y])
            else:
                mileage_to_next_address = float(distances[y][x])

            # Get package with the closest destination to current address
            for package in self.packages:
                x = distances[0].index(self.current_address)
                y = distances[0].index(package_table.search(package).address)
                if distances[x][y] != '':
                    candidate_mileage = float(distances[x][y])
                else:
                    candidate_mileage = float(distances[y][x])

                if candidate_mileage < mileage_to_next_address:
                    next_address = package_table.search(package).address
                    package_to_deliver = package
                    mileage_to_next_address = candidate_mileage

            # drive to next_address
            self.current_address = next_address
            self.mileage += mileage_to_next_address

            # deliver package and update delivery time
            delivery_hour = int(load_time[0] + self.mileage // 18)
            delivery_minute = int(load_time[1] + (self.mileage / 18) % 1 * 60)
            if delivery_minute >= 60:
                delivery_hour += 1
                delivery_minute -= 60
            package_table.search(package_to_deliver).delivery_time = (delivery_hour, delivery_minute)
            self.packages.remove(package_to_deliver)

        # drive truck back to hub
        row = distances[0].index('4001 South 700 East')
        column = distances[0].index(self.current_address)
        distance_back_to_hub = distances[column][row]
        self.current_address = '4001 South 700 East'
        self.mileage += float(distance_back_to_hub)
