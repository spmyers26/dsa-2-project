# Student ID: 011571626

from hashtable import HashTable
from package import Package
from truck import Truck
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

