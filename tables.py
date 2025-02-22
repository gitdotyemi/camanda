import sqlite3

#connecting to a database
conn = sqlite3.connect('tripManagement.db')

#creating a cursor
c = conn.cursor()

#creating a table that stores order information in the database
# c.execute ("""CREATE TABLE orders (
#            orderID text not null,
#            customerName text not null,
#            customerID text not null,
#            pickupLocation text not null,
#            pickupDate text not null,
#            dropoffLocation text not null,
#            dropoffDate text not null,
#            orderStatus text not null check(orderStatus in ('Scheduled', 'In-Transit', 'Completed', 'Canceled')))""")

#creating a table that stores vehicle information in the database
# c.execute  ("""CREATE TABLE vehicles (
#             vehicleID text not null,
#             registrationNumber text not null,
#             makeModel text not null,
#             year text not null,
#             capacity integer not null,
#             fuelType text not null check(fuelType in ('Petrol', 'Diesel', 'Electricity', 'Gas')),
#             fuelEfficiency real not null,
#             vehicleStatus text not null  check(vehicleStatus in ('Available', 'In Transit', 'Under Maintenance')))""")

#creating a table that stores drivers information in the database
# c.execute ("""CREATE TABLE drivers (
#            driversID text not null,
#            driversName text not null,
#            phoneNumber text not null,
#            licenseNumber text not null,
#            vehicleQualification text not null check(vehicleQualification in ('Truck', 'Bike', 'Box Body Van', 'Trailer')),
#            driverStatus text not null check(driverStatus in ('Available', 'In-Transit', 'Unavailable')),
#            yearsOfExperience integer not null)""")

#creating a list of orders
# manyOrders = [('ORD-20251902-1001', 'Odu Modu', 'CUS-1001', 'D12, Scab Estate, Akure, Ondo', '2/19/2025 5:13 PM', 'B4, Araromi Estate, Shagamu, Ogun', '2/21/2025 9:00 AM', 'Scheduled'),
#               ('ORD-20252002-1002', 'jen Li', 'CUS-1002', 'No 24 Shangisha, Magodo, Lagos', '2/20/2025 9:18 AM', 'A9, Guje street,  Kubwa, Abuja', '2/22/2025 10:00 AM', 'In-Transit'),
#               ('ORD-20252002-1003', 'Sam Sung', 'CUS-1003', 'A9, Guje street,  Kubwa, Abuja', '2/20/2025 3:24 PM', 'D12, Scab Estate, Akure, Ondo', '2/22/2025 11:00 AM', 'Canceled'),
#               ('ORD-20252102-1004', 'Temi Tope', 'CUS-1004', 'No 14B, Abuloma, Port-harcourt, Rivers', '2/21/2025 10:00 AM', 'No 24 Shangisha, Magodo, Lagos', '2/23/2025 1:00 PM', 'Completed'),
#               ('ORD-20252102-1005', 'Fola Shade', 'CUS-1005', 'B11, Muji Estate, Ado-ekiti, Ekiti', '2/21/2025 10:13 AM', 'No 14B, Abuloma, Port-harcourt, Rivers', '2/23/2025 2:00 PM', 'Scheduled')]

#inserting multiple drivers information into thhe database
# c.executemany("INSERT INTO orders VALUES (?,?,?,?,?,?,?,?)", manyOrders)

#creating  a list of vehicles
# manyVehicles = [('V0001', 'ABC123', 'Toyota Hino 500', '2019', '10', 'Petrol', '3.50', 'Available'),
#                 ('V0002', 'XYZ789', 'Mercedes Actros', '2021', '15', 'Diesel', '4.00', 'In Transit'),
#                 ('V0003', 'LMN456', 'Volvo FH16', '2020', '20', 'Diesel', '3.80', 'Under Maintenance'),
#                 ('V0004', 'PQRR321', 'DAF XF', '2018', '12', 'Petrol', '3.60', 'Available'),
#                 ('V0005', 'JKL654', 'Scania R450', '2022', '18', 'Electricity', '4.20', 'In Transit')]

#inserting multiple drivers information into the database
# c.executemany("INSERT INTO vehicles VALUES (?,?,?,?,?,?,?,?)", manyVehicles)

#creating a list of drivers
# manyDrivers = [('D001', 'Ahmed Musa', '08123456789', 'ABJ002', 'Bike', 'In-Transit', '8'), 
#                ('D002', 'Chinedu Okafor', '08123456789', 'KAN003', 'Box Body Van', 'Unavailable', '6'), 
#                ('D003', 'Bola Adebayor', '08198765432', 'PHC004', 'Trailer', 'Available', '10'), 
#                ('D004', 'Peter Obi', '08045678912', 'IBD005', 'Trailer', 'In-Transit', '7'), 
#                ('D005', 'Frank Emma', '0123456789', 'AKR192', 'Truck', 'Unavailable', '9')]

#inserting multiple drivers information into thhe database
# c.executemany("INSERT INTO drivers VALUES (?,?,?,?,?,?,?)", manyDrivers)

# Fetch all table names
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()
        
# Loop through each table and fetch its contents
for table in tables:
    table_name = table[0]
    print(f"\n🔹 Table: {table_name}")
            
    # Get column names
    c.execute(f"PRAGMA table_info({table_name});")
    columns = [col[1] for col in c.fetchall()]
    print(f"Columns: {', '.join(columns)}")
            
    # Fetch table contents
    c.execute(f"SELECT * FROM {table_name};")
    rows = c.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No data available.")

#querying the table
# c.execute("SELECT * FROM drivers")

# items = c.fetchall()
# for item in items:
#     print(item)

#commiting to the command
conn.commit()

#closing the command
conn.close()