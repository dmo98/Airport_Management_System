import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    password="password",
    database='AMS_v3'
)

cursor = db.cursor()

# -------------------------CREATE TABLES-------------------------

query = "CREATE TABLE airport(airport_name VARCHAR(60) PRIMARY KEY, city VARCHAR(20), state VARCHAR(20), gm_ssn VARCHAR(11))"
cursor.execute(query)
db.commit()
# print(1)

query = "CREATE TABLE employee(ssn VARCHAR(11) PRIMARY KEY, Fname VARCHAR(20), M VARCHAR(1), Lname VARCHAR(20), phone_number VARCHAR(12), sex VARCHAR(1), age INT, address VARCHAR(100), salary INT, jobtype VARCHAR(20), airport VARCHAR(60), FOREIGN KEY(airport) REFERENCES airport(airport_name) ON DELETE SET NULL)"
cursor.execute(query)
db.commit()
# print(2)

query = "ALTER TABLE airport ADD FOREIGN KEY(gm_ssn) REFERENCES employee(ssn) ON DELETE SET NULL"
cursor.execute(query)
db.commit()
# print(3)
"""

# query = "DESCRIBE airport"
# cursor.execute(query)
# for x in cursor:
#   print(x)

# print('\n')
# query = "DESCRIBE employee"
# cursor.execute(query)
# for x in cursor:
#   print(x)

"""
query = "CREATE TABLE flight(flightID VARCHAR(10) PRIMARY KEY, airline VARCHAR(30), d_airport VARCHAR(60), d_time TIMESTAMP, d_gate VARCHAR(5), a_airport VARCHAR(60), a_time TIMESTAMP, a_gate VARCHAR(5), aircraft_sno INT, FOREIGN KEY(d_airport) REFERENCES airport(airport_name) ON DELETE SET NULL, FOREIGN KEY(a_airport) REFERENCES airport(airport_name) ON DELETE SET NULL)"
cursor.execute(query)
db.commit()
# print(4)

query = "CREATE TABLE flight_crew(passport_number VARCHAR(9) PRIMARY KEY, name_ VARCHAR(30), yrs_exp INT, age INT, sex VARCHAR(1), jobtype VARCHAR(20))"
cursor.execute(query)
db.commit()
# print(5)

query = "CREATE TABLE aircraft(sno INT PRIMARY KEY, model VARCHAR(10), capacity INT, date_of_manufacture DATE)"
cursor.execute(query)
db.commit()
# print(6)

query = "ALTER TABLE flight ADD FOREIGN KEY(aircraft_sno) REFERENCES aircraft(sno) ON DELETE SET NULL"
cursor.execute(query)
db.commit()
# print(7)

query = "CREATE TABLE hangar(airport_name VARCHAR(60), hangarID INT, location VARCHAR(20), PRIMARY KEY(airport_name, hangarID), FOREIGN KEY(airport_name) REFERENCES airport(airport_name) ON DELETE CASCADE)"
cursor.execute(query)
db.commit()
# print(8)

query = "CREATE TABLE crew(flightID VARCHAR(10), passport_number VARCHAR(9), PRIMARY KEY(flightID, passport_number), FOREIGN KEY(flightID) REFERENCES flight(flightID) ON DELETE CASCADE, FOREIGN KEY(passport_number) REFERENCES flight_crew(passport_number) ON DELETE CASCADE)"
cursor.execute(query)
db.commit()
# print(9)

query = "CREATE TABLE undergoes_maintenance(airport_name VARCHAR(60), hangarID INT, aircraft_sno INT, maintenance_type VARCHAR(30), date DATE, PRIMARY KEY(airport_name, hangarID, aircraft_sno), FOREIGN KEY(airport_name, hangarID) REFERENCES hangar(airport_name, hangarID) ON DELETE CASCADE, FOREIGN KEY(aircraft_sno) REFERENCES aircraft(sno) ON DELETE CASCADE)"
cursor.execute(query)
db.commit()
# print(10)

query = "CREATE TABLE works_at(airport_name VARCHAR(60), hangarID INT, emp_ssn VARCHAR(11), PRIMARY KEY(airport_name, hangarID, emp_ssn), FOREIGN KEY(airport_name, hangarID) REFERENCES hangar(airport_name, hangarID) ON DELETE CASCADE, FOREIGN KEY(emp_ssn) REFERENCES employee(ssn) ON DELETE CASCADE)"
cursor.execute(query)
db.commit()
# print(11)

query = "CREATE TABLE specialize_in(emp_ssn VARCHAR(11) PRIMARY KEY, model VARCHAR(10), FOREIGN KEY(emp_ssn) REFERENCES employee(ssn) ON DELETE CASCADE)"
cursor.execute(query)
db.commit()
# print(12)
"""

# query = "SHOW TABLES;"
# cursor.execute(query)
# for x in cursor:
#     print(x)

# print('\n')
# query = "DESCRIBE flight_crew;"
# cursor.execute(query)
# for x in cursor:
#    print(x)

# print('\n')
# query = "DESCRIBE aircraft;"
# cursor.execute(query)
# for x in cursor:
#    print(x)

# print('\n')
# query = "DESCRIBE hangar;"
# cursor.execute(query)
# for x in cursor:
#    print(x)

# print('\n')
# query = "DESCRIBE crew;"
# cursor.execute(query)
# for x in cursor:
#    print(x)

# print('\n')
# query = "DESCRIBE undergoes_maintenance;"
# cursor.execute(query)
# for x in cursor:
#    print(x)

# print('\n')
# query = "DESCRIBE works_at;"
# cursor.execute(query)
# for x in cursor:
#    print(x)

# print('\n')
# query = "DESCRIBE specialize_in;"
# cursor.execute(query)
# for x in cursor:
#    print(x)
"""
# -------------------------POPULATE TABLES-------------------------

# -- populate airport table
query = "INSERT INTO airport (airport_name, city, state) VALUES (%s, %s, %s)"
tuples = [
    ("O'Hare International Airport", 'Chicago', 'Illinois'),
    ("Hartsfield-Jackson Atlanta International Airport", 'Atlanta', 'Georgia'),
    ("John F. Kennedy International Airport", 'New York City', 'New York')
]
cursor.executemany(query, tuples)
db.commit()
# print(1)

# -- populate employee table with the general managers
query = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
tuples = [
    ('123-45-6789', 'Michael','J','Smith','204-888-0632','M',50,'4022 Shingleton Road, Des Plaines, IL, 60018',150000,'Manager',"O'Hare International Airport"),
    ('987-65-4321', 'Frank','D','James','204-564-2378','M',45,'3539 Hillview Drive, Atlanta, GA, 30308',125000,'Manager',"Hartsfield-Jackson Atlanta International Airport"),
    ('456-37-2890', 'James','M','Johnson','204-504-9389','M',50,'1418 Stanley Avenue, New York, NY, 10014',175000,'Manager',"John F. Kennedy International Airport")
]
cursor.executemany(query, tuples)
db.commit()
# print(2)

# -- add gm ssn to airport table
query = "UPDATE airport SET gm_ssn = (%s) WHERE airport_name = (%s)"
values = [
    ('123-45-6789', "O'Hare International Airport"),
    ('987-65-4321', "Hartsfield-Jackson Atlanta International Airport"),
    ('456-37-2890', "John F. Kennedy International Airport")
]
cursor.executemany(query, values)
db.commit()
# print(3)
"""
# cursor.execute("SELECT * FROM airport")
# for x in cursor:
#     print(x)

# cursor.execute("SELECT * FROM employee")
# for x in cursor:
#     print(x)

"""
# -- populate employee table with Customer Service employees
query = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
tuples = [
    ('876-23-4758', 'Marsha', 'D', 'Grisham', '773-425-0584','F',35,'860 Oakmound Road, Chicago, IL, 60018',75000,'Customer Service',"O'Hare International Airport"),
    ('330-24-4930', 'Latonia', 'W', 'Hodge', '773-623-0384','F',49,'4188 Cecil Street, Chicago, IL, 60607',73000,'Customer Service',"O'Hare International Airport"),
    ('532-88-3657', 'Susan', 'E', 'Porter', '708-543-5164','F',27,'1612 Sun Valley Road, Chicago, IL, 60290',65000,'Customer Service',"O'Hare International Airport"),
    ('360-78-6879', 'Kathleen', 'H', 'Duprey', '773-964-4633','F',31,'2935 Victoria Street, Chicago, IL, 60631',78000,'Customer Service',"O'Hare International Airport"),
    ('390-87-5247', 'Darlene', 'M', 'Graham', '402-384-5689','F',55,'419 Cheshire Road, Atlanta, GA, 30340',85000,'Customer Service',"Hartsfield-Jackson Atlanta International Airport"),
    ('536-08-3331', 'Agnes', 'G', 'Boyer', '402-890-5463','F',39,'3272 Chardonnay Drive, Atlanta, GA, 30318',69000,'Customer Service',"Hartsfield-Jackson Atlanta International Airport"),
    ('258-54-6726', 'Rosie', 'S', 'Cunningham', '404-621-9889','F',45,'3293 Musgrave Street, Atlanta, GA, 30312',85000,'Customer Service',"Hartsfield-Jackson Atlanta International Airport"),
    ('671-07-3134', 'Fredrick', 'S', 'Folse', '404-312-5446','M',48,'683 Clement Street, Atlanta, GA, 30318',75000,'Customer Service',"Hartsfield-Jackson Atlanta International Airport"),
    ('055-70-5755', 'Joseph', 'J', 'Ford', '917-569-6185','M',55,'354 Hoffman Avenue, New York, NY, 10013',90000,'Customer Service',"John F. Kennedy International Airport"),
    ('053-44-0035', 'Margaret', 'R', 'Carillo', '646-417-5852','F',43,'1270 Oakwood Avenue, New York, NY, 10022',87000,'Customer Service',"John F. Kennedy International Airport"),
    ('549-27-1913', 'Carlo', 'J', 'Davis', '917-859-5764','M',33,'1158 Williams Avenue, New York, NY, 10001',78000,'Customer Service',"John F. Kennedy International Airport"),
    ('061-20-3172', 'Cynthia', 'T', 'Call', '917-847-1189','F',25,'3210 My Drive, New York, NY, 10013',90000,'Customer Service',"John F. Kennedy International Airport")
]
cursor.executemany(query, tuples)
db.commit()
# print(1)

# -- populate employee table with ground level workers
query = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
tuples = [
    ('568-61-6837', 'Isaac', 'J', 'Campbell', '773-519-3921','M',45,'942 Evergreen Lane, Chicago, IL, 60290',65000,'Ground Level',"O'Hare International Airport"),
    ('337-86-4292', 'David', 'I', 'Gleason', '773-426-6392','M',39,'1421 Johnstown Road, Chicago, IL, 60607',63000,'Ground Level',"O'Hare International Airport"),
    ('354-12-8353', 'Iris', 'M', 'Hancock', '773-879-0023','F',37,'1163 Poplar Street, Chicago, IL, 60606',61000,'Ground Level',"O'Hare International Airport"),
    ('335-28-1206', 'Sarah', 'D', 'Beaulieu', '773-206-3272','F',31,'3360 University Drive, Chicago, IL, 60606',54000,'Ground Level',"O'Hare International Airport"),
    ('667-28-1080', 'Oren', 'K', 'Warren', '762-207-3373','M',45,'1635 Flint Street, Atlanta, GA, 30303',75000,'Ground Level',"Hartsfield-Jackson Atlanta International Airport"),
    ('673-20-4106', 'Michele', 'F', 'Mallory', '404-514-3999','F',29,'4641 College Street, Atlanta, GA, 30303',64000,'Ground Level',"Hartsfield-Jackson Atlanta International Airport"),
    ('387-76-2842', 'Donna', 'M', 'Ramirez', '678-770-7254','F',35,'3678 Irish Lane, Atlanta, GA, 30301',65000,'Ground Level',"Hartsfield-Jackson Atlanta International Airport"),
    ('668-28-0486', 'Lea', 'H', 'Peele', '770-639-5484','F',28,'2907 Junior Avenue, Atlanta, GA, 30305',72000,'Ground Level',"Hartsfield-Jackson Atlanta International Airport"),
    ('076-24-0014', 'Tracey', 'J', 'Rosado', '646-925-2255','F',35,'1344 Forest Avenue, New York, NY, 10013',72000,'Ground Level',"John F. Kennedy International Airport"),
    ('086-52-7069', 'Anna', 'C', 'Hiles', '646-853-0675','F',33,'2833 Farnum Road, New York, NY, 10007',77000,'Ground Level',"John F. Kennedy International Airport"),
    ('056-44-0593', 'Marvin', 'H', 'Walton', '917-537-5865','M',53,'4883 Long Street, New York, NY, 10011',78000,'Ground Level',"John F. Kennedy International Airport"),
    ('066-56-8658', 'Mildred', 'P', 'Becker', '917-374-7158','F',39,'1606 Oakwood Avenue, New York, NY, 10022',80000,'Ground Level',"John F. Kennedy International Airport")
]
cursor.executemany(query, tuples)
db.commit()
# print(2)

# -- populate employee table with engineers/technicians
query = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
tuples = [
    ('325-16-9185', 'Christopher', 'C', 'Jackson', '773-870-2657','M',25,'1200 Victoria Street, Chicago, IL, 60631',85000,'Engineer',"O'Hare International Airport"),
    ('322-72-5989', 'Janeen', 'J', 'Clark', '847-820-8843','F',29,'3552 University Drive, Chicago, IL, 60607',83000,'Engineer',"O'Hare International Airport"),
    ('341-28-0957', 'Jeremy', 'H', 'Noel', '773-315-3620','M',37,'3050 Virginia Street, Chicago, IL, 60606',91000,'Engineer',"O'Hare International Airport"),
    ('327-98-8421', 'Janet', 'D', 'White', '773-447-6316','F',31,'1149 John Calvin Drive, Chicago, IL, 60606',90000,'Engineer',"O'Hare International Airport"),
    ('259-57-7403', 'Margarita', 'R', 'Hilliard', '404-542-6098','F',45,'2587 Musgrave Street, Atlanta, GA, 30309',95000,'Engineer',"Hartsfield-Jackson Atlanta International Airport"),
    ('257-82-1234', 'Nathaniel', 'C', 'Davis', '470-375-6389','M',39,'139 Lakeland Park Drive, Atlanta, GA, 30339',94000,'Engineer',"Hartsfield-Jackson Atlanta International Airport"),
    ('670-05-5965', 'Arthur', 'J', 'Groves', '404-952-7785','M',35,'3218 Despard Street, Atlanta, GA, 30303',95000,'Engineer',"Hartsfield-Jackson Atlanta International Airport"),
    ('366-36-4978', 'Ruth', 'C', 'Mueller', '402-300-7169','F',26,'4832 Hart Ridge Road, Atlanta, GA, 30305',82000,'Engineer',"Hartsfield-Jackson Atlanta International Airport"),
    ('129-16-7964', 'Robert', 'E', 'Traul', '646-591-6369','M',48,'3259 Duncan Avenue, New York, NY, 10007',102000,'Engineer',"John F. Kennedy International Airport"),
    ('065-70-6759', 'Jose', 'E', 'Seefeldt', '646-250-9152','M',43,'1457 Small Street, New York, NY, 10017',97000,'Engineer',"John F. Kennedy International Airport"),
    ('134-88-0069', 'Joseph', 'M', 'Swanson', '917-292-0581','M',30,'3930 Angus Road, New York, NY, 10019',94000,'Engineer',"John F. Kennedy International Airport"),
    ('111-32-3166', 'Rita', 'A', 'Johnson', '917-817-1338','F',39,'3944 Bicetown Road, New York, NY, 10013',100000,'Engineer',"John F. Kennedy International Airport")
]
cursor.executemany(query, tuples)
db.commit()
# print(3)
"""

"""
# -- populate the aircraft table
query = "INSERT INTO aircraft VALUES (%s, %s, %s, %s)"
tuples = [
    (1, 'B737-800', 162, '2001-01-24'),
    (2, 'B737-800', 162, '2008-10-16'),
    (3, 'B737-800', 162, '1998-02-06'),
    (4, 'A320', 150, '2016-12-03'),
    (5, 'A320', 150, '2012-03-20'),
    (6, 'A320', 150, '2009-03-04'),
    (7, 'E175', 78, '2000-01-09'),
    (8, 'E175', 78, '2003-11-02'),
    (9, 'E175', 78, '1994-11-27'),
    (10, 'A320', 150, '2005-03-16'),
    (11, 'A320', 150, '2011-06-22'),
    (12, 'A320', 150, '2016-07-31'),
    (13, 'A320', 150, '2015-01-17'),
    (14, 'A320', 150, '2008-05-05'),
    (15, 'E175', 78, '2011-12-18'),
    (16, 'B737-800', 162, '2002-06-16'),
    (17, 'B737-800', 162, '2000-01-27'),
    (18, 'E175', 78, '2001-09-01')
]
cursor.executemany(query, tuples)
db.commit()
# print(1)

# -- populate the flight table
query = "INSERT INTO flight VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
tuples = [
    ('DL0650', 'Delta Airlines', "Hartsfield-Jackson Atlanta International Airport",'2021-10-30 14:35:00', 'H10', "John F. Kennedy International Airport", '2021-10-30 16:46:00', 'J14', 1),
    ('DL1143', 'Delta Airlines', "Hartsfield-Jackson Atlanta International Airport",'2021-10-30 19:20:00', 'H10', "John F. Kennedy International Airport", '2021-10-30 21:29:00', 'J14', 2),
    ('DL0860', 'Delta Airlines', "Hartsfield-Jackson Atlanta International Airport",'2021-10-30 09:56:00', 'H10', "John F. Kennedy International Airport", '2021-10-30 12:10:00', 'J14', 3),
    ('DL2822', 'Delta Airlines', "Hartsfield-Jackson Atlanta International Airport",'2021-10-30 07:50:00', 'H11', "O'Hare International Airport", '2021-10-30 08:50:00', 'O06', 4),
    ('DL1725', 'Delta Airlines', "Hartsfield-Jackson Atlanta International Airport",'2021-10-30 10:15:00', 'H11', "O'Hare International Airport", '2021-10-30 11:16:00', 'O06', 5),
    ('DL2864', 'Delta Airlines', "Hartsfield-Jackson Atlanta International Airport",'2021-10-30 12:20:00', 'H11', "O'Hare International Airport", '2021-10-30 13:24:00', 'O06', 6),
    ('DL5493', 'Delta Airlines', "O'Hare International Airport",'2021-10-30 06:55:00', 'O04', "John F. Kennedy International Airport", '2021-10-30 10:03:00', 'J17', 7),
    ('DL5710', 'Delta Airlines', "O'Hare International Airport",'2021-10-30 10:48:00', 'O04', "John F. Kennedy International Airport", '2021-10-30 13:51:00', 'J17', 8),
    ('DL5616', 'Delta Airlines', "O'Hare International Airport",'2021-10-30 14:30:00', 'O04', "John F. Kennedy International Airport", '2021-10-30 17:41:00', 'J17', 9),
    ('AA9222', 'American Airlines', "Hartsfield-Jackson Atlanta International Airport",'2021-10-30 07:00:00', 'H12', "John F. Kennedy International Airport", '2021-10-30 09:13:00', 'J16', 10),
    ('AA9264', 'American Airlines', "Hartsfield-Jackson Atlanta International Airport",'2021-10-30 16:20:00', 'H12', "John F. Kennedy International Airport", '2021-10-30 18:30:00', 'J16', 11),
    ('AA9123', 'American Airlines', "Hartsfield-Jackson Atlanta International Airport",'2021-10-30 08:59:00', 'H12', "John F. Kennedy International Airport", '2021-10-30 11:08:00', 'J16', 12),
    ('AA1574', 'American Airlines', "Hartsfield-Jackson Atlanta International Airport",'2021-10-30 18:07:00', 'H13', "O'Hare International Airport", '2021-10-30 19:08:00', 'O08', 13),
    ('AA1300', 'American Airlines', "Hartsfield-Jackson Atlanta International Airport",'2021-10-30 10:25:00', 'H13', "O'Hare International Airport", '2021-10-30 11:28:00', 'O08', 14),
    ('AA3511', 'American Airlines', "Hartsfield-Jackson Atlanta International Airport",'2021-10-30 15:10:00', 'H13', "O'Hare International Airport", '2021-10-30 16:27:00', 'O08', 15),
    ('AA1378', 'American Airlines', "O'Hare International Airport",'2021-10-30 12:44:00', 'O05', "John F. Kennedy International Airport", '2021-10-30 15:47:00', 'J18', 16),
    ('AA1301', 'American Airlines', "O'Hare International Airport",'2021-10-30 15:50:00', 'O05', "John F. Kennedy International Airport", '2021-10-30 21:03:00', 'J18', 17),
    ('AA9235', 'American Airlines', "O'Hare International Airport",'2021-10-30 13:15:00', 'O05', "John F. Kennedy International Airport", '2021-10-30 17:03:00', 'J18', 18)
]
cursor.executemany(query, tuples)
db.commit()
#print(2)

# -- populate flight table with return flights
query = "INSERT INTO flight VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
tuples = [
    ('DL0651', 'Delta Airlines', "John F. Kennedy International Airport",'2021-11-01 14:35:00', 'J14', "Hartsfield-Jackson Atlanta International Airport", '2021-11-01 16:46:00', 'H10', 1),
    ('DL1144', 'Delta Airlines', "John F. Kennedy International Airport",'2021-11-01 19:20:00', 'J14', "Hartsfield-Jackson Atlanta International Airport", '2021-11-01 21:29:00', 'H10', 2),
    ('DL0861', 'Delta Airlines', "John F. Kennedy International Airport",'2021-11-01 09:56:00', 'J14', "Hartsfield-Jackson Atlanta International Airport", '2021-11-01 12:10:00', 'H10', 3),
    ('DL2823', 'Delta Airlines', "O'Hare International Airport",'2021-11-01 07:50:00', 'O06', "Hartsfield-Jackson Atlanta International Airport", '2021-11-01 08:50:00', 'H11', 4),
    ('DL1726', 'Delta Airlines', "O'Hare International Airport",'2021-11-01 10:15:00', 'O06', "Hartsfield-Jackson Atlanta International Airport", '2021-11-01 11:16:00', 'H11', 5),
    ('DL2865', 'Delta Airlines', "O'Hare International Airport",'2021-11-01 12:20:00', 'O06', "Hartsfield-Jackson Atlanta International Airport", '2021-11-01 13:24:00', 'H11', 6),
    ('DL5494', 'Delta Airlines', "John F. Kennedy International Airport",'2021-11-01 06:55:00', 'J17', "O'Hare International Airport", '2021-11-01 10:03:00', 'O04', 7),
    ('DL5711', 'Delta Airlines', "John F. Kennedy International Airport",'2021-11-01 10:48:00', 'J17', "O'Hare International Airport", '2021-11-01 13:51:00', 'O04', 8),
    ('DL5617', 'Delta Airlines', "John F. Kennedy International Airport",'2021-11-01 14:30:00', 'J17', "O'Hare International Airport", '2021-11-01 17:41:00', 'O04', 9),
    ('AA9223', 'American Airlines', "John F. Kennedy International Airport",'2021-11-01 07:00:00', 'J16', "Hartsfield-Jackson Atlanta International Airport", '2021-11-01 09:13:00', 'H12', 10),
    ('AA9265', 'American Airlines', "John F. Kennedy International Airport",'2021-11-01 16:20:00', 'J16', "Hartsfield-Jackson Atlanta International Airport", '2021-11-01 18:30:00', 'H12', 11),
    ('AA9124', 'American Airlines', "John F. Kennedy International Airport",'2021-11-01 08:59:00', 'J16', "Hartsfield-Jackson Atlanta International Airport", '2021-11-01 11:08:00', 'H12', 12),
    ('AA1575', 'American Airlines', "O'Hare International Airport",'2021-11-01 18:07:00', 'O08', "Hartsfield-Jackson Atlanta International Airport", '2021-11-01 19:08:00', 'H13', 13),
    ('AA1299', 'American Airlines', "O'Hare International Airport",'2021-11-01 10:25:00', 'O08', "Hartsfield-Jackson Atlanta International Airport", '2021-11-01 11:28:00', 'H13', 14),
    ('AA3512', 'American Airlines', "O'Hare International Airport",'2021-11-01 15:10:00', 'O08', "Hartsfield-Jackson Atlanta International Airport", '2021-11-01 16:27:00', 'H13', 15),
    ('AA1379', 'American Airlines', "John F. Kennedy International Airport",'2021-11-01 12:44:00', 'J18', "O'Hare International Airport", '2021-11-01 15:47:00', 'O05', 16),
    ('AA1302', 'American Airlines', "John F. Kennedy International Airport",'2021-11-01 15:50:00', 'J18', "O'Hare International Airport", '2021-11-01 21:03:00', 'O05', 17),
    ('AA9236', 'American Airlines', "John F. Kennedy International Airport",'2021-11-01 13:15:00', 'J18', "O'Hare International Airport", '2021-11-01 17:03:00', 'O05', 18)
]
cursor.executemany(query, tuples)
db.commit()
# print(2)
"""

# cursor.execute("SELECT * FROM flight WHERE d_time > '2021-11-01 13:15:00')
# for x in cursor:
#     print(x)

"""
# -- populate the flight_crew table
query = "INSERT INTO flight_crew VALUES (%s, %s, %s, %s, %s, %s)"
tuples = [
    ('546829653', 'Keisha T Wallace', 15, 42, 'F', 'Pilot-Captain'),
    ('420484971', 'Sarah G Foley', 7, 29, 'F', 'Pilot-First Officer'),
    ('907887501', 'Nancy T Phillips', 10, 37, 'F', 'Flight Attendant'),
    ('821157897', 'Jimmy M Davis', 25, 56, 'M', 'Flight Attendant'),
    ('725208287', 'Matthew D Rodriguez', 19, 44, 'M', 'Pilot-Captain'),
    ('928631416', 'John J Whiteaker', 11, 37, 'M', 'Pilot-First Officer'),
    ('100909199', 'Marie N Erwin', 2, 24, 'F', 'Flight Attendant'),
    ('892024783', 'Anthony D Lugo', 5, 29, 'M', 'Flight Attendant'),
    ('422581953', 'Joseph P Castaneda', 25, 57, 'M', 'Pilot-Captain'),
    ('382307854', 'Trista C Robinson', 13, 42, 'F', 'Pilot-First Officer'),
    ('782458020', 'Kristy B Polston', 1, 23, 'F', 'Flight Attendant'),
    ('462341113', 'Ronald K Moore', 2, 26, 'M', 'Flight Attendant'),
    ('968944560', 'Jack C Hubbs', 8, 33, 'M', 'Pilot-Captain'),
    ('403401374', 'Christopher S Cash', 7, 29, 'M', 'Pilot-First Officer'),
    ('846487034', 'Mary E Robinson', 15, 37, 'F', 'Flight Attendant'),
    ('999407928', 'Cecile S Arroyo', 5, 30, 'F', 'Flight Attendant'),
    ('793164877', 'Alton G Brown', 30, 56, 'M', 'Pilot-Captain'),
    ('818744786', 'David L Stevenson', 7, 31, 'M', 'Pilot-First Officer'),
    ('144861342', 'David H Jester', 8, 35, 'M', 'Flight Attendant'),
    ('405513003', 'Carolyn J Valdes', 5, 28, 'F', 'Flight Attendant'),
    ('225815180', 'Sarah R Brent', 15, 42, 'F', 'Pilot-Captain'),
    ('764936757', 'Esther M Rider', 13, 39, 'F', 'Pilot-First Officer'),
    ('793780651', 'Eileen R White', 19, 45, 'F', 'Flight Attendant'),
    ('343192698', 'Cindy J Gilbert', 10, 36, 'F', 'Flight Attendant'),
    ('305054206', 'Timothy S Moore', 25, 52, 'M', 'Pilot-Captain'),
    ('824931648', 'Florinda N Harris', 11, 35, 'F', 'Pilot-First Officer'),
    ('902296895', 'Dominic L Johnson', 8, 33, 'M', 'Flight Attendant'),
    ('380745787', 'Lucy K Bragg', 5, 29, 'F', 'Flight Attendant'),
    ('188501599', 'Jerry M Curtis', 30, 60, 'M', 'Pilot-Captain'),
    ('982015967', 'Pamela R Smith', 14, 39, 'F', 'Pilot-First Officer'),
    ('499143554', 'John R West', 10, 39, 'M', 'Flight Attendant'),
    ('572134238', 'Stephen A McGee', 12, 36, 'M', 'Flight Attendant'),
    ('623948865', 'Joseph C Jackson', 15, 40, 'M', 'Pilot-Captain'),
    ('586125128', 'Emma D Hope', 8, 32, 'F', 'Pilot-First Officer'),
    ('639480480', 'Cynthia A Dion', 1, 24, 'F', 'Flight Attendant'),
    ('411433144', 'Carla N Alvarez', 3, 26, 'F', 'Flight Attendant'),
    ('458827923', 'Tracy L Pena', 7, 30, 'F', 'Pilot-Captain'),
    ('382656167', 'Carl G Woodruff', 5, 29, 'M', 'Pilot-First Officer'),
    ('675293019', 'William A Gomez', 30, 57, 'M', 'Flight Attendant'),
    ('503067404', 'James E Reilly', 3, 27, 'M', 'Flight Attendant'),
    ('718374651', 'Jimmy G Roush', 24, 49, 'M', 'Pilot-Captain'),
    ('796676229', 'Alicia J Willingham', 5, 29, 'F', 'Pilot-First Officer'),
    ('989077034', 'Samantha O Hofman', 19, 43, 'F', 'Flight Attendant'),
    ('470048212', 'Lisa T Rich', 17, 46, 'F', 'Flight Attendant'),
    ('298574842', 'Beatrice F Matheny', 12, 42, 'F', 'Pilot-Captain'),
    ('232263423', 'Brian J Clark', 3, 29, 'M', 'Pilot-First Officer'),
    ('351332893', 'Maria R Moreno', 11, 37, 'F', 'Flight Attendant'),
    ('406671248', 'Lola M Pierce', 20, 46, 'M', 'Flight Attendant'),
    ('971735759', 'Mona N Rodriguez', 14, 42, 'F', 'Pilot-Captain'),
    ('765274117', 'Martha E Barlow', 9, 35, 'F', 'Pilot-First Officer'),
    ('211218261', 'Ray S Hinton', 22, 46, 'M', 'Flight Attendant'),
    ('797200686', 'Leroy M Franklin', 10, 36, 'M', 'Flight Attendant'),
    ('141611986', 'Howard F Taylor', 16, 42, 'M', 'Pilot-Captain'),
    ('823056602', 'Virginia M Willis', 2, 24, 'F', 'Pilot-First Officer'),
    ('990284956', 'Ken R Knight', 11, 37, 'M', 'Flight Attendant'),
    ('898726099', 'Michael T Pryor', 12, 36, 'M', 'Flight Attendant'),
    ('495269464', 'Pete A Myers', 14, 44, 'M', 'Pilot-Captain'),
    ('529777314', 'Bob B Byers', 4, 29, 'M', 'Pilot-First Officer'),
    ('389305568', 'Annie B Henderson', 1, 27, 'F', 'Flight Attendant'),
    ('768281236', 'Michael K Larson', 2, 26, 'M', 'Flight Attendant'),
    ('917690624', 'Corey C Kirsch', 17, 42, 'M', 'Pilot-Captain'),
    ('793446686', 'Wendy J Stevenson', 5, 29, 'F', 'Pilot-First Officer'),
    ('257223046', 'William J Brown', 8, 33, 'M', 'Flight Attendant'),
    ('856265809', 'Nathalie E Evans', 12, 36, 'F', 'Flight Attendant'),
    ('616642531', 'Mandy A Fullwood', 15, 42, 'F', 'Pilot-Captain'),
    ('806280731', 'Edward S Asher', 6, 29, 'M', 'Pilot-First Officer'),
    ('800424295', 'Brian H Galasso', 9, 32, 'M', 'Flight Attendant'),
    ('142802800', 'Derrick G Perri', 12, 40, 'M', 'Flight Attendant'),
    ('781487838', 'Brian L Downs', 24, 52, 'M', 'Pilot-Captain'),
    ('893617708', 'Linda P Bogart', 12, 35, 'F', 'Pilot-First Officer'),
    ('360751315', 'Richard J Brooks', 7, 37, 'M', 'Flight Attendant'),
    ('953736008', 'Jimmy M Davis', 2, 26, 'M', 'Flight Attendant')
]
cursor.executemany(query, tuples)
db.commit()
# print(1)

# -- populate the crew table
query = "INSERT INTO crew VALUES (%s, %s)"
tuples = [
    ('DL0650', '546829653'),
    ('DL0650', '420484971'),
    ('DL0650', '907887501'),
    ('DL0650', '821157897'),
    ('DL1143', '725208287'),
    ('DL1143', '928631416'),
    ('DL1143', '100909199'),
    ('DL1143', '892024783'),
    ('DL0860', '422581953'),
    ('DL0860', '382307854'),
    ('DL0860', '782458020'),
    ('DL0860', '462341113'),
    ('DL2822', '968944560'),
    ('DL2822', '403401374'),
    ('DL2822', '846487034'),
    ('DL2822', '999407928'),
    ('DL1725', '793164877'),
    ('DL1725', '818744786'),
    ('DL1725', '144861342'),
    ('DL1725', '405513003'),
    ('DL2864', '225815180'),
    ('DL2864', '764936757'),
    ('DL2864', '793780651'),
    ('DL2864', '343192698'),
    ('DL5493', '305054206'),
    ('DL5493', '824931648'),
    ('DL5493', '902296895'),
    ('DL5493', '380745787'),
    ('DL5710', '188501599'),
    ('DL5710', '982015967'),
    ('DL5710', '499143554'),
    ('DL5710', '572134238'),
    ('DL5616', '623948865'),
    ('DL5616', '586125128'),
    ('DL5616', '639480480'),
    ('DL5616', '411433144'),
    ('AA9222', '458827923'),
    ('AA9222', '382656167'),
    ('AA9222', '675293019'),
    ('AA9222', '503067404'),
    ('AA9264', '718374651'),
    ('AA9264', '796676229'),
    ('AA9264', '989077034'),
    ('AA9264', '470048212'),
    ('AA9123', '298574842'),
    ('AA9123', '232263423'),
    ('AA9123', '351332893'),
    ('AA9123', '406671248'),
    ('AA1574', '971735759'),
    ('AA1574', '765274117'),
    ('AA1574', '211218261'),
    ('AA1574', '797200686'),
    ('AA1300', '141611986'),
    ('AA1300', '823056602'),
    ('AA1300', '990284956'),
    ('AA1300', '898726099'),
    ('AA3511', '495269464'),
    ('AA3511', '529777314'),
    ('AA3511', '389305568'),
    ('AA3511', '768281236'),
    ('AA1378', '917690624'),
    ('AA1378', '793446686'),
    ('AA1378', '257223046'),
    ('AA1378', '856265809'),
    ('AA1301', '616642531'),
    ('AA1301', '806280731'),
    ('AA1301', '800424295'),
    ('AA1301', '142802800'),
    ('AA9235', '781487838'),
    ('AA9235', '893617708'),
    ('AA9235', '360751315'),
    ('AA9235', '953736008')
]
cursor.executemany(query, tuples)
db.commit()
# print(2)

# -- populate crew table for return flights
query = "INSERT INTO crew VALUES (%s, %s)"
tuples = [
    ('DL0651', '546829653'),
    ('DL0651', '420484971'),
    ('DL0651', '907887501'),
    ('DL0651', '821157897'),
    ('DL1144', '725208287'),
    ('DL1144', '928631416'),
    ('DL1144', '100909199'),
    ('DL1144', '892024783'),
    ('DL0861', '422581953'),
    ('DL0861', '382307854'),
    ('DL0861', '782458020'),
    ('DL0861', '462341113'),
    ('DL2823', '968944560'),
    ('DL2823', '403401374'),
    ('DL2823', '846487034'),
    ('DL2823', '999407928'),
    ('DL1726', '793164877'),
    ('DL1726', '818744786'),
    ('DL1726', '144861342'),
    ('DL1726', '405513003'),
    ('DL2865', '225815180'),
    ('DL2865', '764936757'),
    ('DL2865', '793780651'),
    ('DL2865', '343192698'),
    ('DL5494', '305054206'),
    ('DL5494', '824931648'),
    ('DL5494', '902296895'),
    ('DL5494', '380745787'),
    ('DL5711', '188501599'),
    ('DL5711', '982015967'),
    ('DL5711', '499143554'),
    ('DL5711', '572134238'),
    ('DL5617', '623948865'),
    ('DL5617', '586125128'),
    ('DL5617', '639480480'),
    ('DL5617', '411433144'),
    ('AA9223', '458827923'),
    ('AA9223', '382656167'),
    ('AA9223', '675293019'),
    ('AA9223', '503067404'),
    ('AA9265', '718374651'),
    ('AA9265', '796676229'),
    ('AA9265', '989077034'),
    ('AA9265', '470048212'),
    ('AA9124', '298574842'),
    ('AA9124', '232263423'),
    ('AA9124', '351332893'),
    ('AA9124', '406671248'),
    ('AA1575', '971735759'),
    ('AA1575', '765274117'),
    ('AA1575', '211218261'),
    ('AA1575', '797200686'),
    ('AA1299', '141611986'),
    ('AA1299', '823056602'),
    ('AA1299', '990284956'),
    ('AA1299', '898726099'),
    ('AA3512', '495269464'),
    ('AA3512', '529777314'),
    ('AA3512', '389305568'),
    ('AA3512', '768281236'),
    ('AA1379', '917690624'),
    ('AA1379', '793446686'),
    ('AA1379', '257223046'),
    ('AA1379', '856265809'),
    ('AA1302', '616642531'),
    ('AA1302', '806280731'),
    ('AA1302', '800424295'),
    ('AA1302', '142802800'),
    ('AA9236', '781487838'),
    ('AA9236', '893617708'),
    ('AA9236', '360751315'),
    ('AA9236', '953736008')
]
cursor.executemany(query, tuples)
db.commit()
# print(3)
"""

# cursor.execute("SELECT COUNT(*) FROM flight_crew")
# for x in cursor:
#     print(x)

# cursor.execute("SELECT COUNT(*) FROM crew")
# for x in cursor:
#     print(x)

"""
# -- SLIGHT CHANGE IN TABLES
# -- drop capacity column from aircraft
query = "ALTER TABLE aircraft DROP COLUMN capacity"
cursor.execute(query)
db.commit()
print(1)

# -- create a separate table for the aircraft models and use the model as an attribute in the relationship specialize_in
query = "CREATE TABLE aircraft_model(model VARCHAR(10) PRIMARY KEY, CAPACITY INT)"
cursor.execute(query)
db.commit()
print(2)

# -- populate aircraft_model table
query = "INSERT INTO aircraft_model VALUES (%s, %s)"
tuples = [
    ('B737-800', 162),
    ('A320', 150),
    ('E175', 78)
]
cursor.executemany(query, tuples)
db.commit()
# print(3)

# -- add manufacturer to aircraft_model table
query = "ALTER TABLE aircraft_model ADD manufacturer VARCHAR(10)"
cursor.execute(query)
db.commit()
# print(4)

query = "UPDATE aircraft_model SET manufacturer = 'Boeing' WHERE model LIKE 'B%'"
cursor.execute(query)
db.commit()
# print(5)

query = "UPDATE aircraft_model SET manufacturer = 'Airbus' WHERE model LIKE 'A%'"
cursor.execute(query)
db.commit()
# print(6)

query = "UPDATE aircraft_model SET manufacturer = 'Embraer' WHERE model LIKE 'E%'"
cursor.execute(query)
db.commit()
# print(7)

query = "ALTER TABLE aircraft ADD FOREIGN KEY(model) REFERENCES aircraft_model(model) ON DELETE SET NULL"
cursor.execute(query)
db.commit()
print(8)

query = "ALTER TABLE specialize_in ADD FOREIGN KEY(model) REFERENCES aircraft_model(model) ON DELETE SET NULL"
cursor.execute(query)
db.commit()
# print(9)

# -- populate the specialize_in table
query = "INSERT INTO specialize_in VALUES (%s, %s)"
tuples = [
    ('325-16-9185', 'B737-800'),
    ('322-72-5989', 'A320'),
    ('341-28-0957', 'E175'),
    ('327-98-8421', 'B737-800'),
    ('259-57-7403', 'B737-800'),
    ('257-82-1234', 'A320'),
    ('670-05-5965', 'A320'),
    ('366-36-4978', 'E175'),
    ('129-16-7964', 'B737-800'),
    ('065-70-6759', 'B737-800'),
    ('134-88-0069', 'A320'),
    ('111-32-3166', 'E175')
]
cursor.executemany(query, tuples)
db.commit()
# print(1)

# -- populate the hangar table
query = "INSERT INTO hangar VALUES (%s, %s, %s)"
tuples = [
    ("O'Hare International Airport", 1, "North"),
    ("O'Hare International Airport", 2, "South-East"),
    ("O'Hare International Airport", 3, "North-West"),
    ("Hartsfield-Jackson Atlanta International Airport", 1, "South"),
    ("Hartsfield-Jackson Atlanta International Airport", 2, "North-East"),
    ("Hartsfield-Jackson Atlanta International Airport", 3, "West"),
    ("John F. Kennedy International Airport", 1, "East"),
    ("John F. Kennedy International Airport", 2, "North"),
    ("John F. Kennedy International Airport", 3, "South-West")
]
cursor.executemany(query, tuples)
db.commit()
# print(2)

# -- populate the works_at table
query = "INSERT INTO works_at VALUES (%s, %s, %s)"
tuples = [
    ("O'Hare International Airport", 1, '325-16-9185'),
    ("O'Hare International Airport", 2, '322-72-5989'),
    ("O'Hare International Airport", 3, '341-28-0957'),
    ("O'Hare International Airport", 1, '327-98-8421'),
    ("Hartsfield-Jackson Atlanta International Airport", 1, '259-57-7403'),
    ("Hartsfield-Jackson Atlanta International Airport", 2, '257-82-1234'),
    ("Hartsfield-Jackson Atlanta International Airport", 2, '670-05-5965'),
    ("Hartsfield-Jackson Atlanta International Airport", 3, '366-36-4978'),
    ("John F. Kennedy International Airport", 1, '129-16-7964'),
    ("John F. Kennedy International Airport", 2, '065-70-6759'),
    ("John F. Kennedy International Airport", 3, '134-88-0069'),
    ("John F. Kennedy International Airport", 3, '111-32-3166')
]
cursor.executemany(query, tuples)
db.commit()
# print(3)

# -- populate the undergoes_maintenance table
query = "INSERT INTO undergoes_maintenance VALUES (%s, %s, %s, %s, %s)"
tuples = [
    ("O'Hare International Airport", 3, 7, 'Repaired Flaps', '2021-10-29'),
    ("O'Hare International Airport", 3, 8, 'Autopilot Software Update', '2021-10-30'),
    ("O'Hare International Airport", 3, 9, 'General Maintenance', '2021-10-29'),
    ("O'Hare International Airport", 2, 14, 'General Maintenance', '2021-10-31'),
    ("Hartsfield-Jackson Atlanta International Airport", 1, 1, 'Repaired Rudder', '2021-10-29'),
    ("Hartsfield-Jackson Atlanta International Airport", 1, 2, 'General Maintenance', '2021-10-29'),
    ("Hartsfield-Jackson Atlanta International Airport", 2, 10, 'General Maintenance', '2021-10-29'),
    ("Hartsfield-Jackson Atlanta International Airport", 2, 11, 'Painted', '2021-10-28'),
    ("John F. Kennedy International Airport", 1, 16, 'Engine Tests', '2021-10-31'),
    ("John F. Kennedy International Airport", 2, 17, 'Autopilot Software Update', '2021-10-31'),
    ("John F. Kennedy International Airport", 3, 18, 'Brake Check', '2021-10-31'),
    ("Hartsfield-Jackson Atlanta International Airport", 2, 4, 'General Maintenance', '2021-11-01'),
    ("Hartsfield-Jackson Atlanta International Airport", 1, 3, 'Repaired Rudder', '2021-11-01'),
    ("Hartsfield-Jackson Atlanta International Airport", 2, 5, 'Spoilers Testing', '2021-11-01'),
    ("Hartsfield-Jackson Atlanta International Airport", 2, 6, 'Autopilot Software Update', '2021-11-02'),
    ("Hartsfield-Jackson Atlanta International Airport", 2, 12, 'Engine Tests', '2021-11-02'),
    ("Hartsfield-Jackson Atlanta International Airport", 2, 13, 'Spoilers Testing', '2021-11-02'),
    ("Hartsfield-Jackson Atlanta International Airport", 3, 15, 'Paint Job', '2021-11-02')
]
cursor.executemany(query, tuples)
db.commit()
# print(4)