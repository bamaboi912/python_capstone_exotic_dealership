import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database=db_name
        )
        print("MySQL Database Connection Successful")
    except Error as err:
        print(f"Error {err}")
    return connection



def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: {err}")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query sucessful")
    except Error as err:
        print(f"Error: {err}")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: {err}")


#Queries
create_database_query = "create database EXOTIC_DEALERSHIP"

#create coupe table
create_coupe_table = """
create table COUPE_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
year integer NOT NULL,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL,
engine VARCHAR(50) NOT NULL,
date_of_arrival VARCHAR(50) NOT NULL,
days_on_the_lot integer NOT NULL);"""


#create sedan table
create_sedan_table = """
create table SEDAN_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
year integer NOT NULL,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL,
engine VARCHAR(50) NOT NULL,
date_of_arrival VARCHAR(50) NOT NULL,
days_on_the_lot integer NOT NULL);"""

#create SUV table
create_SUV_table = """
create table SUV_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
year integer NOT NULL,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL,
engine VARCHAR(50) NOT NULL,
date_of_arrival VARCHAR(50) NOT NULL,
days_on_the_lot integer NOT NULL);"""

#create truck table
create_truck_table = """
create table TRUCK_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
year integer NOT NULL,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL,
engine VARCHAR(50) NOT NULL,
date_of_arrival VARCHAR(50) NOT NULL,
days_on_the_lot integer NOT NULL);"""

#create directory table
create_directory_table = """
create table DIRECTORY_INFORMATION(
employees_ID VARCHAR(12) PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
employee_position VARCHAR(50) NOT NULL,
salary integer NOT NULL,
phone_number VARCHAR(10) NOT NULL,
years_of_experience integer NOT NULL);"""

#create Customer Information table
create_customer_information_table = """
create table CUSTOMER_INFORMATION(
full_name VARCHAR(50) PRIMARY KEY,
address VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
phone_number VARCHAR(50) NOT NULL,
birthday VARCHAR(50) NOT NULL,
social_security_number VARCHAR(50) NOT NULL,
job_title VARCHAR(50) NOT NULL,
monthly_income integer NOT NULL);"""


#populate coupe table
coupe_vehicles = """ 
insert into COUPE_MODELS values
('123abc321',2017,'Ashton Martin', 'Vanquish', 200, 115000, 'V8','2/18/2023',10),
('123abc322',2023,'Porsche', '911', 2002, 125000, 'V8','1/18/2023',5),
('123abc323',2017,'Subaru', 'BRZ', 3000, 28000, 'V6','4/18/2023',30),
('123abc324',2016,'Dodge', 'Challenger', 20, 30000, 'V8','3/14/2023',15),
('123abc325',2020,'BMW', 'M4', 100, 74000, 'V8','5/18/2023',1),
('123abc326',2021,'McLaren', 'Artura', 300, 233000, 'V8','7/19/2023',17),
('123abc327',2019,'Ford', 'Mustang', 50000, 27000, 'V6','9/8/2023',50),
('123abc328',2022,'Audi', 'TT', 200, 52000, 'V8','10/1/2023',10)"""

#populate sedan table
sedan_vehicles = """ 
insert into SEDAN_MODELS values
('123abc321',2017,'Nissan', 'Versa', 200, 25000, 'V6','2/18/2023',10),
('123abc322',2023,'Honda', 'Civic', 2002, 35000, 'V8','1/18/2023',5),
('123abc323',2017,'Honda', 'Civic Si', 3000, 28000, 'V6','4/18/2023',30),
('123abc324',2016,'Hyundai ', 'Elantra N', 20, 30000, 'V8','3/14/2023',15),
('123abc325',2020,'Mazda', '3', 100, 40000, 'V8','5/18/2023',1),
('123abc326',2021,'Volkswagen ', 'Jetta GLI', 300, 33000, 'V8','7/19/2023',17),
('123abc327',2019,'BMW', 'i4', 50000, 27000, 'V6','9/8/2023',50),
('123abc328',2022,'Cadillac', 'CT4-V Blackwing', 200, 52000, 'V8','10/1/2023',10)"""


#populate suv table
suv_vehicles = """ 
insert into SUV_MODELS values
('123abc321',2017,'RANGE', 'ROVER SPORT', 200, 85000, 'V6','2/18/2023',10),
('123abc322',2023,'Genesis', 'GV70', 2002, 45000, 'V8','1/18/2023',5),
('123abc323',2017,'BMW', 'X3', 3000, 28000, 'V6','4/18/2023',30),
('123abc324',2016,'Mercedes-Benz ', 'GLC', 20, 50000, 'V8','3/14/2023',15),
('123abc325',2020,'Maserati', 'Grecale ', 100, 104000, 'V8','5/18/2023',1),
('123abc326',2021,'Mercedes-Benz', 'GLB', 300, 33000, 'V8','7/19/2023',17),
('123abc327',2019,'Volvo', 'XC60', 50000, 27000, 'V6','9/8/2023',50),
('123abc328',2022,'Jaguar', 'F-Pace', 200, 52000, 'V8','10/1/2023',10)"""



#populate truck table
truck_vehicles = """ 
insert into TRUCK_MODELS values
('123abc321',2017,'Ford', 'Maverick', 200, 85000, 'V6','2/18/2023',10),
('123abc322',2023,'Ford ', 'F-150 Raptor', 2002, 75000, 'V8','1/18/2023',5),
('123abc323',2017,'Ram', '1500', 3000, 28000, 'V6','4/18/2023',30),
('123abc324',2016,'Ram ', '1500 TRX', 20, 50000, 'V8','3/14/2023',15),
('123abc325',2020,'Chevy', 'Silverado EV', 100, 104000, 'V8','5/18/2023',1),
('123abc326',2021,'Chevy', 'Silverado HD', 300, 33000, 'V8','7/19/2023',17),
('123abc327',2019,'Nissan', 'Frontier', 50000, 27000, 'V6','9/8/2023',50),
('123abc328',2022,'Nissan', 'TITAN XD', 200, 52000, 'V8','10/1/2023',10)"""

#populate directory table
employee_information = """
insert into DIRECTORY_INFORMATION values
('58641', 'Steve','Martin', 'corporate manager',150000,'8209875267',15),
('58642', 'Shayla','Stark', 'branch manager',130000,'8209875269,12),
('58643', 'Tevin','Williams', 'regional manager',120000,8209875260,8),
('58644', 'Chris','Smith', 'regional manager',120000,8209875165,8),
('58645', 'Bryan','Hope', 'store manager',62000,8209875263,5),
('58646', 'Crystal','Hathowrne', 'store manager',60000,8209875264,5),
('58647', 'Michelle','Gay', 'sales representative',55000,8209879254,4),
('58648', 'Deshawn','Matthews', 'sales representative',90000,8209877415,10),
('58649', 'Justin','Bradford', 'sales representative',50000,8209870121,3),
('58610', 'Kim','Lee', 'sales representative',80000,8209873351,7),
('58611', 'Reed','Martinez', 'sales representative',70000,8209878452,6),
('58612', 'Harrison','Wells', 'mechanic',50000,8205675265,3),
('58613', 'Matt','Stevens', 'mechanic',52000,8202875265,4),
('58614', 'Alexis','Bell', 'mechanic',62000,8205875265,8),
('58615', 'Mike','Marshall', 'mechanic',45000,8208795466,2),
('58616', 'Aaron','Mase', 'mechanic',41000,8209586724,1)
"""

#populate customer table
customer_information = """
insert into CUSTOMER_INFORMATION values
( 'Chris Martin', '213 W Colfax Denver Co 80233', 'chrisM@gmailcom' ,'8209875267','10/02/1996', '654-25-8546','Clerk',4600),
( 'Joe Matthew', '564 Standford dr Tampa Fl 33220', 'jmatt021@gmailcom' ,'8209875261','11/05/1996', '254-25-7546','unemployment',2000),
( 'Kamisha Burns', '589 Englewood dr Denver Co 80243', 'burns@yahoocom' ,'8209875262','9/04/1989', '554-25-8546','mechanic',4200),
( 'Krystal Martin', '214 Flemming st Denver Co 80233', 'kMbaddie@gmailcom' ,'8209875263','01/02/1996', '254-25-8546','insurance sales',4000),
( 'Jamal Vargas', '987 Coastal rd Greenwood SC 75216', 'jayv2@gmailcom' ,'8209875264','08/02/1987', '354-25-8546','',5500),
( 'Brook Smith', '637 S Ave Denver Co 80211', 'ilovny@hotmailcom' ,'8209875265','03/02/1996', '454-25-8546','Clerk',3500),
( 'James McKnight', '2564 Ohio cir Clevand OH 45215', 'jmcknight@gmailcom' ,'8209875266','07/02/1990', '954-25-8546','corporate manager',8000),
( 'Jazmine Martinez', '4524 W Fort Hood Tx 95852', 'jazzyM@gmailcom' ,'8209875268','10/02/1999', '754-25-8546','branch manager',7000),
( 'Ashley King', '761 E Brookes st Talladega Al 95482', 'kingash@gmailcom' ,'8209875269','7/22/1998', '854-25-8546','gas station',5000),
( 'Mike Harden', '99885 Nevada st Colorado Springs Co 80654', 'mikegohard@gmailcom' ,'8209875277','10/20/1996', '154-25-8546','police',4500)"""



#read values from coupe table
display_coupe_models_table = """
SELECT * FROM COUPE_MODELS;
"""

#read values from sedan table
display_sedan_models_table = """
SELECT * FROM SEDAN_MODELS;
"""

#read values from SUV table
display_SUV_models_table = """
SELECT * FROM SUV_MODELS;
"""

#read values from truck table
display_truck_models_table = """
SELECT * FROM TRUCK_MODELS;
"""

#read values from directory table
display_directory_table = """
SELECT * FROM DIRECTORY_INFORMATION;
"""

#read values from customer info table
display_customer_information_table = """
SELECT * FROM CUSTOMER_INFORMATION;
"""








connection = create_server_connection("localhost", "root", "student","exotic_dealership")
results = read_query(connection, display_coupe_models_table)
execute_query(connection,customer_information)
for result in results:
    print(result)