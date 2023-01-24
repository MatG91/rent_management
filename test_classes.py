# This is the section to test the classes.py

from classes import Property, Tenant, Reservation


property = Property('Via Panzini')

tenant = Tenant('Matteo', 'matt@matt.com', property.id)

reserve1 = Reservation('2023-03-10', '2023-03-20', tenant.id)

reserve2 = Reservation('2023-03-21', '2023-03-31', tenant.id)

reserve3 = Reservation('2023-04-21', '2023-04-29', tenant.id)
reserve4 = Reservation('2023-03-21', '2023-03-29', tenant.id)


print(reserve3.add_reservation())
reserve1.add_reservation()
reserve2.add_reservation()
reserve4.add_reservation()
