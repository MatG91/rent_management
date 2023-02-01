import csv
from datetime import datetime
from functions import check_overlap

# Creating a class for the property


class Property:
    id = 0
# When we instanciate Property class we need to instanciate name of the property

    def __init__(self, name):
        Property.id += 1
        self.id = name + str(Property.id)
        self.name = name

    # This method write the details of the property to the csv file

    def to_csv(self):
        with open('./properties.csv', mode='a') as csv_file:
            fieldnames = ['id', 'name']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(
                {'id': self.id, 'name': self.name})


# Creating a class for a tenant
class Tenant:
    id = 0
    # Instanciate new tenant with name, email and unique identifier. property_ID is the foreign key of property class table

    def __init__(self, name, email, property_id):
        Tenant.id += 1
        self.id = name + str(Tenant.id)
        self.name = name
        self.email = email
        self.property_id = property_id


# This method write the details of the tenant to the csv file

    def to_csv(self):
        with open('./tenants.csv', mode='a') as csv_file:
            fieldnames = ['id', 'name', 'email', 'property ID']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(
                {'id': self.id, 'name': self.name, 'email': self.email, 'property ID': self.property_id})


# Creating a class for the reservation
class Reservation:
    id = 0
    header = False
    # Instanciate new reservation with tenant ID, start date, end date

    def __init__(self, start_date, end_date, tenant_id):
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            print('Invalid date format, it should be YYYY-MM-DD')
            return
        Reservation.id += 1
        self.id = str(tenant_id) + str(Reservation.id)
        self.start_date = start_date
        self.end_date = end_date
        self.tenant_id = tenant_id
# This method checks if there is any overlapping booking. If none write in the csv

    def add_reservation(self):
        if check_overlap(self.start_date.date(), self.end_date.date()):
            return self.to_csv()


# This method write the details of the reservation to the csv file

    def to_csv(self):
        with open('./reservations.csv', mode='a') as csv_file:
            fieldnames = ['id', 'start_date', 'end_date', 'tenant_id']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if not Reservation.header:
                writer.writeheader()
                Reservation.header = True
            writer.writerow(
                {'id': self.id, 'start_date': self.start_date.date(), 'end_date': self.end_date.date(), 'tenant_id': self.tenant_id})
