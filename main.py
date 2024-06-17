# Student ID: 011571626

from hashtable import HashTable
from package import Package
from truck import Truck
from user_interface import UserInterface
import csv

package_table = HashTable()

# read package data
with open('package_file.csv', newline='') as csvfile:
    package_reader = csv.reader(csvfile, delimiter=',')

    # create package objects and insert into hashtable
    for package_info in package_reader:
        package_id = int(package_info[0])
        address = package_info[1]
        city = package_info[2]
        zip_code = package_info[4]
        deadline = package_info[5]
        weight = package_info[6]
        package = Package(package_id, address, city, zip_code, deadline, weight)
        package_table.insert(package_id, package)

distances = []

# read distance data
with open('distance_table.csv', newline='') as csvfile:
    distance_reader = csv.reader(csvfile, delimiter=',')

    for distance in distance_reader:
        distances.append(distance)
distances[0][17] = '3575 W Valley Central Station bus Loop'

# Creating trucks to load deliver packages
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()
trucks = [truck1, truck2, truck3]

# loading truck1 at 8:00 AM
truck1.packages = [1, 13, 14, 15, 19, 20, 29, 30, 31, 34, 37, 40, 21, 16, 4, 7]
for package_id in truck1.packages:
    package = package_table.search(package_id)
    package.load_time = (8, 0)

# truck 1 departs for deliveries at 8:00 AM
truck1.deliver_packages(package_table, distances, (8, 0))

# loading truck2 at 9:05 AM, after delayed packages arrive
truck2.packages = [2, 3, 5, 6, 8, 10, 11, 12, 17, 18, 25, 28, 32, 36, 38, 22]
for package_id in truck2.packages:
    package = package_table.search(package_id)
    package.load_time = (9, 5)

# truck2 departs for delivery at 9:05 AM
truck2.deliver_packages(package_table, distances, (9, 5))

# loading truck 3 at 10:20, after incorrect address is updated
truck3.packages = [9, 23, 24, 26, 27, 33, 35, 39]
for package_id in truck3.packages:
    package = package_table.search(package_id)
    package.load_time = (10, 20)

# truck3 departs for deliveries at 10:20 AM, as driver of truck1 has returned
truck3.deliver_packages(package_table, distances, (10, 20))

# start the user interface
ui = UserInterface()
ui.main_menu(package_table, trucks)
