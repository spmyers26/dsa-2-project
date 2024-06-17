from datetime import datetime


class UserInterface:
    def __init__(self):
        self.main_menu_input = None
        # self.hour_input = None
        # self.minute_input = None
        # self.am_pm_input = None

    def main_menu(self, package_table, trucks):
        print('Welcome to the WGUPS package routing service\n')
        while self.main_menu_input != 'Exit':
            print('1. Check package status by time')
            print('2. Check all package statuses by time')
            print('3. Check total truck mileage')

            self.main_menu_input = input('Please enter a command or \'Exit\' to quit program\n')
            if self.main_menu_input == '1':
                self.package_status(package_table)
            elif self.main_menu_input == '2':
                self.all_package_statuses(package_table)
            elif self.main_menu_input == '3':
                self.truck_mileage(trucks)
            elif self.main_menu_input.lower() == 'exit':
                exit(1)
            else:
                print('Command not recognized. Please enter a valid command (1-3) or \'Exit\' to exit program\n')

        print('Goodbye! Thank you for using the WGUPS package routing service')

    def package_status(self, package_table):
        valid_package_input = False
        valid_time_input = False

        while not valid_package_input:
            package_id_input = input('Enter a Package ID (1-40)\n')
            try:
                if 1 <= int(package_id_input) <= 40:
                    valid_package_input = True
                    package = package_table.search(int(package_id_input))
                else:
                    print('Package ID out of range (1-40). Please enter a valid Package ID')
            except TypeError:
                print('Invalid input')

        while not valid_time_input:
            time_input = input('Enter a time to check package status (12:00 AM - 11:59 PM)\n')
            try:
                status_time = datetime.strptime(time_input, '%I:%M %p')
                valid_time_input = True
                print(f'At {time_input}, {package.__str__((status_time.hour, status_time.minute))}')
            except ValueError:
                try:
                    status_time = datetime.strptime(time_input, '%I:%M%p')
                    valid_time_input = True
                    print(f'At {time_input}, {package.__str__((status_time.hour, status_time.minute))}')
                except ValueError:
                    print('Time input not in recognized format (HH:MM AM/PM)')

    def all_package_statuses(self, package_table):
        valid_time_input = False
        while not valid_time_input:
            time_input = input('Enter a time to check package status (12:00 AM - 11:59 PM)\n')
            try:
                status_time = datetime.strptime(time_input, '%I:%M %p')
                valid_time_input = True
            except ValueError:
                try:
                    status_time = datetime.strptime(time_input, '%I:%M%p')
                    valid_time_input = True
                except ValueError:
                    print('Time input not in recognized format (HH:MM AM/PM)')

        for i in range(1, 41):
            package = package_table.search(i)
            print(f'At {time_input}, {package.__str__((status_time.hour, status_time.minute))}')
        print('\n')

    def truck_mileage(self, trucks):
        total_mileage = 0
        for truck in trucks:
            total_mileage += truck.mileage
        print(f'Total mileage: {round(total_mileage, 2)}')
