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
create table DIRECTORY_INFORMATON(
employees_ID VARCHAR(12) PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
employee_position VARCHAR(50) NOT NULL,
salary integer NOT NULL,
phone_number integer NOT NULL,
years_of_experience integer NOT NULL);"""

#create Customer Information table
create_customer_information_table = """
create table CUSTOMER_INFORMATON(
full_name VARCHAR(12) PRIMARY KEY,
address VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
phone_number integer NOT NULL,
birthday VARCHAR(50) NOT NULL,
social_security_number integer NOT NULL,
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




connection = create_server_connection("localhost", "root", "student","exotic_dealership")

execute_query(connection,create_customer_information_table)